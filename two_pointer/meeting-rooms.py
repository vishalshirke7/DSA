"""
https://www.interviewbit.com/old/problems/meeting-rooms/
"""


#OWN
def solve(self, A):
    arr = [val[0] for val in A]
    dep = [val[1] for val in A]
    arr = sorted(arr)
    dep = sorted(dep)
    arr_ptr, dep_ptr = 0, 0
    max_rooms = cur_rooms = 0
    while arr_ptr < len(A) and dep_ptr < len(A):
        if arr[arr_ptr] < dep[dep_ptr]:
            cur_rooms += 1
            arr_ptr += 1
        else:
            cur_rooms -= 1
            dep_ptr += 1
        max_rooms = max(max_rooms, cur_rooms)
    return max_rooms
