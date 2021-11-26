"""
https://www.interviewbit.com/old/problems/first-non-repeating-character-in-a-stream-of-characters/
"""

# own worked
def solve(A):
    count_map = dict()
    queue = [0] * 100000
    start_ptr, end_ptr, ans = 0, 0, ''
    for index in range(len(A)):
        char = A[index]
        if char in count_map:
            count_map[char] += 1
            while start_ptr < end_ptr and count_map[queue[start_ptr]] > 1:
                start_ptr += 1
        else:
            count_map[char] = count_map.get(char, 0) + 1
            queue[end_ptr] = char
            end_ptr += 1
        if queue[start_ptr] == 0:
            ans += '#'
        else:
            ans += queue[start_ptr]
    return ans



print('Output', solve("abadbc"))
print('Output', solve("abcabc"))
print('Output', solve("gu"))
print('Output', solve("iergxwhddh"))
print('Output', solve("jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"))


# editorial
def solve(self, A):
    queue = []
    visited = set()
    repeated = set()
    res = []
    for ele in A:
        if ele not in visited:
            queue.append(ele)
            visited.add(ele)
        elif ele not in repeated:
            repeated.add(ele)
            queue.remove(ele)
        letter = queue[0] if len(queue) > 0 else '#'
        res.append(letter)
    return ''.join(res)
            