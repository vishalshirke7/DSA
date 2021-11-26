"""
https://www.interviewbit.com/old/problems/flip/
"""

def flip(A):
    output = list()
    start = local_diff = max_diff = 0
    for index, val in enumerate(A):
        local_diff += 1 if val is '0' else -1
        if local_diff < 0:
            start = index + 1
            local_diff = 0
            continue
        if local_diff > max_diff:
            max_diff = local_diff
            output = [start + 1, index + 1]
    return output


def flip(A):
    output = list()
    start = current_ones = max_ones = 0
    for end in range(len(A)):
        if A[end] == '0':
            current_ones += 1
            if current_ones > max_ones:
                max_ones = current_ones
                output = [start + 1, end + 1]
        else:
            current_ones -= 1
            if current_ones < 0:
                start = end + 1
                current_ones = 0
    return output

print('Output', flip("010"))
print('Output', flip("0110010"))
print('Output', flip("0110110"))