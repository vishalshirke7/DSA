"""
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

"""

def is_substring_with_rotation(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    if size1 != size2:
        return False
    string1_string1 = string1 + string1
    if string2 in string1_string1:
        return True
    return False


print(is_substring_with_rotation('ACDA', 'ACAD'))