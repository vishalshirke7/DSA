"""
https://leetcode.com/problems/compare-version-numbers/
"""

def compareVersion(version1, version2):
    v1_list, v2_list = version1.split('.'), version2.split('.')
    v1_len, v2_len = len(v1_list), len(v2_list)
    diff = 0
    v1_number = int("".join(map(lambda val: str(int(val)), v1_list)))
    v2_number = int("".join(map(lambda val: str(int(val)), v2_list)))
    if v1_len > v2_len:
        diff = v1_len - v2_len
        v2_number *= (10 ** diff)
    elif v2_len > v1_len:
        diff = v2_len - v1_len
        v1_number *= (10 ** diff)

    if v1_number > v2_number:
        return 1
    elif v2_number > v1_number:
        return -1
    else:
        return 0


print('Output', compareVersion("1.01", "1.001"))  
print('Output', compareVersion("1.0", "1.0.0"))  
print('Output', compareVersion("0.1", "1.1"))  
print('Output', compareVersion("1.0.1", "1"))  
print('Output', compareVersion("7.5.2.4", "7.5.3"))   