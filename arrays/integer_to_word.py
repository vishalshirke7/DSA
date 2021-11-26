ONES = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN',
        'ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
TENS = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']
HUNDREDS = 'HUNDRED'
BIGS = ['', 'THOUSAND', 'LAKH', 'CRORE']

def concat_words(parts, reverse=False):
    concatenated_word = ""
    print(parts)
    if reverse:
        for word in parts:
            concatenated_word = word + " " + concatenated_word
    else:
        for word in parts:
            concatenated_word += word + " "
    return concatenated_word[:-1]

def convert_in_parts(number):
    parts = list()
    if number >= 100:
        parts.append(ONES[number // 100])
        parts.append(HUNDREDS)
        number %= 100
    if 10 <= number <= 19:
        parts.append(ONES[number])
    elif number >= 20:
        parts.append(TENS[number // 10])
        number %= 10
    if 1 <= number <= 9:
        parts.append(ONES[number])
    return concat_words(parts)

def convert_number_to_word(number):
    divisor = 1000
    final_word = ""
    parts_count = 0
    final_word_parts = list()
    if number==0 :
        return ONES[0]
    while(number > 0):
        parts = convert_in_parts(number % divisor) + " " + BIGS[parts_count]
        parts_count += 1
        final_word_parts.append(parts)
        number //= divisor
        divisor = 100
    print("FINAL WORD - ", concat_words(final_word_parts, reverse=True))

convert_number_to_word(1234)