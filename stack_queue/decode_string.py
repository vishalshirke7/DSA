"""
https://leetcode.com/problems/decode-string/
"""


def decodeString(s):
    stack = list()
    current_number = 0
    decoded_string = ""
    for character in s:
        if character == '[':
            stack.append(decoded_string)
            stack.append(current_number)
            decoded_string = ""
            current_number = 0
        elif character == ']':
            number = stack.pop()
            prev_string = stack.pop()
            decoded_string = prev_string + number * decoded_string
        elif character.isdigit():
            current_number = current_number * 10 + int(character)
        else:
            decoded_string += character

    print('decoded_string', decoded_string)

decodeString('3[a2[c]]')
# decodeString('abc3[cd]xyz')


"""
Using recursion - https://leetcode.com/problems/decode-string/discuss/87544/Clean-C%2B%2B-Recursive-Solution-with-Explanation
"""