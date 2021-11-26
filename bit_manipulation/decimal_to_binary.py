def decimal_to_binary(decimal):
    if decimal == 0:
        return '0000'
    binary_string = ""
    while decimal > 0:
        binary_string = str(decimal % 2) + binary_string
        decimal /= 2 
    return binary_string

print(decimal_to_binary(25332525070235))