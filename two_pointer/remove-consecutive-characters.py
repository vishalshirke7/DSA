"""
https://www.interviewbit.com/problems/remove-consecutive-characters/
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""

# STACK
def solve(A, B):
    stack = list()
    for char in A:
        if stack and stack[-1][0] == char:
            stack[-1][1] = stack[-1][1] + 1
            if stack[-1][1] == B:
                stack.pop()
        else:
            stack.append([char, 1])
    return "".join(char * cnt for char, cnt in stack)


def solve(s, k):
    s = list(s)
    cur_ptr = 0
    count_map = [1] * len(s)
    for index in range(len(s)):
        s[cur_ptr] = s[index]
        if cur_ptr > 0 and s[cur_ptr] == s[cur_ptr - 1]:
            count_map[cur_ptr] = count_map[cur_ptr - 1] + 1
        else:
            count_map[cur_ptr] = 1
        if count_map[cur_ptr] == k:
            cur_ptr -= k
        cur_ptr += 1
    return "".join(s[:cur_ptr])


def solve(A, B):
    output = ''
    i = 0
    while i<len(A):
        block = ''
        temp = A[i]
        count = 0
        while (A[i]==temp):
            count += 1
            block += A[i]
            i += 1
            if i==len(A):
                break
        if count !=B:
            output += block

# print('Output', solve("aabcd", 2))
# print('Output', solve("aaagccc", 3))
print('Output', solve("abcddcbsa", 2))
print('Output', solve("dtpdtaaaaaaaaappppppppppppppppppppaaaaaaaaaaxxxxxxxxxxxxxxsssssssssjjjjjjjjjjjjjjjjjjjjxxxxxxxxxxxxxxxxxxxxsssssssjjjjjjjjjjjjjjjjjjjjssssxxxxxxatdwvvpctpggggggggggggggggggggajagglaaaaaaaaaaaaaaaaaaaa", 20))