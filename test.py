import json
import time
import redis

import constants
import slack_api_manager, database_manager as db_manager


class PortfolioCoreInvestmentsManager(object):
    """Provides portfolio core investments
    Args:
        portfolio_type_id - client level/family level
        portfolio_identifier - client_id/family_id
    """

    def __init__(self, portfolio_type_id, portfolio_identifier):
        self.portfolio_type_id = portfolio_type_id
        self.portfolio_identifier = portfolio_identifier
        self.database_manager = db_manager.DatabaseManager()
        self.database_connector_data = self.database_manager.create_connections()

    def _segregate_funds_and_schemes(self, current_value, result_row_dict, instrument_data):
        fund_name = result_row_dict.get('fund_name')
        scheme_name = result_row_dict.get('scheme_name')
        instrument_data[fund_name] = instrument_data.get(fund_name, {})
        instrument_data[fund_name]['current_value'] = instrument_data[fund_name].get('current_value', 0) + current_value
        instrument_data[fund_name][scheme_name] = instrument_data[fund_name].get(fund_name, {})
        instrument_data[fund_name][scheme_name]['transaction_units'] = instrument_data[fund_name][scheme_name].get('transaction_units', 0) + float(result_row_dict.get('units'))
        instrument_data[fund_name][scheme_name]['current_value'] = instrument_data[fund_name][scheme_name].get('current_value', 0) + current_value
        return instrument_data
        
    def _format_result_row(self, result_row):
        result_row_dict = dict(result_row._asdict())
        if result_row_dict.get('fund_name'):
            if 'Structured Products' in result_row_dict['fund_name']:
                result_row_dict['fund_name'] = result_row_dict['scheme_name']
        return result_row_dict        

    def _aggregate_core_investments_data(self, model_data_list):
        """Aggregate portfolio holdings at various levels
          Output dictionary format:-
            {
               "MEDIUM RISK ASSET":{
                  "current_value":7421743.316115001,
                  "MF-Equity":{
                     "current_value":7421743.316115001,
                     "Large & Mid Cap Fund":{
                        "current_value":1781501.0659400001,
                        "Canara Robeco Emerging Equities (G)":{
                           "current_value":564817.88844
                        },
                        "Invesco India Growth Opportunities Fund (G)":{
                           "current_value":1216683.1775
                        }
                     }
                  }
               }
            }
        """
        aggregated_core_investments_data = dict()
        for result_row in model_data_list:
            result_row_dict = self._format_result_row(result_row)
            risk_name = result_row_dict.get('risk_name')
            current_value = float(result_row_dict.get('current_value'))
            instrument_name = result_row_dict.get('instrument_name')
            if risk_name and instrument_name and instrument_name not in ['NA']:
                aggregated_core_investments_data[risk_name] = aggregated_core_investments_data.get(risk_name, {})
                aggregated_core_investments_data[risk_name]['current_value'] = aggregated_core_investments_data[risk_name].get('current_value', 0) + current_value
                aggregated_core_investments_data[risk_name][instrument_name] = aggregated_core_investments_data[risk_name].get(instrument_name, {})
                aggregated_core_investments_data[risk_name][instrument_name]['current_value'] = aggregated_core_investments_data[risk_name][instrument_name].get('current_value', 0) + current_value
                aggregated_core_investments_data[risk_name][instrument_name].update(self._segregate_funds_and_schemes(current_value,
                                                                                                                      result_row_dict,
                                                                                                                      aggregated_core_investments_data[risk_name][instrument_name]))
        return aggregated_core_investments_data

    def _format_core_investments_data(self, asset_class_data):
        investments_data_list = list()

        def _format_schemes_data(schemes_data):
            schemes = list()
            for scheme_name, data in schemes_data.items():
                if type(data) is dict:
                    level_4_data = {
                        'name': scheme_name,
                        'current_value': data['current_value'],
                        'transaction_units': data['transaction_units']
                    }
                    schemes.append(level_4_data)
            return schemes

        def _format_funds_data(instrument_name, funds_data):
            funds = list()
            for fund_name, data in funds_data.items():
                if type(data) is dict:
                    level_3_data = {
                        'name': fund_name,
                        'current_value': data['current_value']
                    }                    
                    if instrument_name in ['Structured Products -Debt', 'Structured Products -Equity']:
                        level_3_data['name'] = ''
                        level_3_data['current_value'] = 0
                    level_3_data['schemes'] = _format_schemes_data(data)
                    funds.append(level_3_data)
            return funds        

        def _format_instruments_data(instruments_data):
            instruments = list()
            for instrument_name, data in instruments_data.items():
                if type(data) is dict:
                    temp_instrument_name = instrument_name
                    if instrument_name in ['Structured Products -Debt', 'Structured Products -Equity', 'Structured Products']:
                        temp_instrument_name = 'Market Linked Debentures'
                    level_2_data = {
                        'name': temp_instrument_name,
                        'current_value': data['current_value']
                    }
                    level_2_data['funds'] = _format_funds_data(instrument_name, data)
                    instruments.append(level_2_data)
            return instruments

        for risk_name, risk_data in asset_class_data.items():
            level_1_data = {
                'name': risk_name,
                'instruments': list(),
                'current_value': risk_data['current_value']
            }
            level_1_data['instruments'] = _format_instruments_data(risk_data)
            investments_data_list.append(level_1_data)
        return investments_data_list

    def _client_porfolio_core_investments_data(self, client_id):
        client_holdings_model_data = self.database_manager.get_client_level_holding_statement_model_data(
                  self.database_connector_data['mysql_engine'], client_id)
        aggregated_core_investments_data = self._aggregate_core_investments_data(client_holdings_model_data)
        client_porfolio_core_investments_data = {
            'core_investments_data': self._format_core_investments_data(aggregated_core_investments_data)
        }
        return client_porfolio_core_investments_data

    def _family_porfolio_core_investments_data(self, family_id):
        family_holdings_model_data = self.database_manager.get_family_level_holding_statement_model_data(
                  self.database_connector_data['mysql_engine'], family_id)
        aggregated_core_investments_data = self._aggregate_core_investments_data(family_holdings_model_data)
        family_porfolio_core_investments_data = {
            'core_investments_data': self._format_core_investments_data(aggregated_core_investments_data)
        }
        return family_porfolio_core_investments_data

    def perform_tasks(self):
        """Perform following tasks:
            1. if portfolio_type_id is of client type, get client level portfolio summary
            2. if portfolio_type_id is of family type, get family level portfolio summary
            Output dictionary format:- 
                [
                   {
                      "name":"MEDIUM RISK ASSET",
                      "instruments":[
                         {
                            "name":"MF-Equity",
                            "current_value":7421743.316115001,
                            "funds":[
                               {
                                  "name":"Focused Fund",
                                  "current_value":994026.8524980001,
                                  "schemes":[
                                     {
                                        "name":"SBI Focused Equity Fund (G)",
                                        "current_value":994026.8524980001
                                     }
                                  ]
                               }
                            ]
                         }
                      ],
                      "current_value":7421743.316115001
                   }
                ]
        """
        porfolio_core_investments_data = dict()
        if self.portfolio_type_id in [constants.PORTFOLIO_TYPE_ID_MAP['client']]:
            porfolio_core_investments_data = self._client_porfolio_core_investments_data(self.portfolio_identifier)
        if self.portfolio_type_id in [constants.PORTFOLIO_TYPE_ID_MAP['family']]:
            porfolio_core_investments_data = self._family_porfolio_core_investments_data(self.portfolio_identifier)
        return porfolio_core_investments_data

def _slack_alert(context, request_data, error):
    """Manages slack alert in case of programmatic failures (5XX status_code)
    """    
    alert_message = ""
    alert_data = {
        '*PORTFOLIO_TYPE_ID:* ': request_data['portfolio_type_id'],
        '*PORTFOLIO_IDENTIFIER:* ': request_data['portfolio_identifier'],
        '*API:* ': 'PORTFOLIO_CORE_INVESTMENTS',
        '*AWS_REQUEST_ID:* ': context.aws_request_id,
        '*CLOUDWATCH_LOG_STREAM_NAME:* ': context.log_stream_name,
        '*ERROR:* ': error,
    }
    for key, value in alert_data.items():
        alert_message += key + str(value) + '\n'
    slack_api_manager.SlackAPIManager().send_message(alert_message)

def _lambda_response_data(context, request_data):
    """Constructs reponse data for lambda
        Output dictionary format:-
        {
           "data":{
              "core_investments_data": []
           }
        }
    """    
    response_data = {
        'data': dict()
    }
    try:
        porfolio_core_investments_data = PortfolioCoreInvestmentsManager(int(request_data['portfolio_type_id']),
                                                                         request_data['portfolio_identifier']).perform_tasks()
        if porfolio_core_investments_data.get('core_investments_data'):
            response_data['data'] = porfolio_core_investments_data
        else:
            response_data['message'] = constants.NO_DATA_FOUND_MESSAGE
        return constants.HTTP_200_OK, response_data
    except Exception as error:
        _slack_alert(context, request_data, error)
        print("Error at PortfolioCoreInvestmentsManager.perform_tasks", str(error))
        return constants.HTTP_500_SERVER_ERROR, response_data

def lambda_handler(event, context):
    """Handles lambda request/response
        Request data format:-
        {
           "portfolio_type_id":1,
           "portfolio_identifier":1681696
        }
    """    
    response_data = dict()
    start_time = time.time()
    request_data = event.get('queryStringParameters', {})
    # redis_client = redis.Redis(host='arwealth-pwm-clientapp-ro.nxjdlw.ng.0001.aps1.cache.amazonaws.com', port=6379, db=0)
    print("REQUEST_DATA", request_data)
    if request_data.get('portfolio_type_id') and request_data.get('portfolio_identifier'):
        # cache_hash_parent_key = 'core_investments'
        # if redis_client.hget(cache_hash_parent_key, request_data['portfolio_identifier']):
        #     response_status_code = 200
        #     response_data = json.loads(redis_client.hget(cache_hash_parent_key, request_data['portfolio_identifier']))
        # else:
        response_status_code, response_data = _lambda_response_data(context, request_data)
        # if response_data.get('data'):
        #     redis_client.hset(cache_hash_parent_key, request_data['portfolio_identifier'], json.dumps(response_data))
    else:
        response_status_code = constants.HTTP_400_BAD_REQUEST
    print("RESPONSE_DATA", response_data)        
    result = {
        'statusCode': response_status_code,
        'body': json.dumps(response_data),
        'headers': constants.RESPONSE_DATA_HEADERS
    }
    print("TOTAL TIME", time.time() - start_time)
    return result