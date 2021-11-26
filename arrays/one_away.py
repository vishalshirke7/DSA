"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
->
pales, pale ->
pale, bale ->
pale, bake ->
pale,
ple
true
true
true
false
"""

def _common_character_count(str_1, str_2, str_1_len, str_2_len):
    common_count = 0
    if str_1_len == str_2_len:
        for i in range(str_1_len):
            if str_1[i] == str_2[i]:
                common_count += 1
    str_1_index, str_2_index = 0, 0
    while(str_1_index < str_1_len and str_2_index < str_2_len):
        if str_1[str_1_index] == str_2[str_2_index]:
            common_count += 1
            str_1_index += 1
            str_2_index += 1
        else:
            if str_1_len > str_2_len:
                str_1_index += 1
            else:
                str_2_index += 1
    return common_count

def one_away(str_1, str_2):
    str_1_len = len(str_1)
    str_2_len = len(str_2)
    if int(str_1_len - str_2_len) > 1:
        return False
    common_character_count = _common_character_count(str_1, str_2, str_1_len, str_2_len)
    if str_1_len == str_2_len:
        if common_character_count >= (str_2_len-1):
            return True 
        return False
    if common_character_count < min(str_1_len, str_2_len):
        return False
    return True

one_away('pale', 'ple')
one_away('pales', 'pale')
one_away('pale', 'bale')
one_away('pale', 'bake')
one_away('bake', 'bake')
