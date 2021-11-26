"""
https://www.interviewbit.com/old/problems/hotel-bookings-possible/
https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
"""


def hotel(arrive, depart, K):
    guests = 0
    events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
    events = sorted(events)
    for event in events:
        if event[1] == 1:
            guests += 1
        else:
            guests -= 1

        if guests > K:
            return 0
    return 1

def hotel(A, B, K):
    A.sort()
    B.sort()
    for i in range(len(A)):
        if i + K < len(A) and A[i+K] < B[i]:
            return False
    return True

# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]
# arr = [1,3,4]
# dep = [12, 8, 6]
# arr = [1, 2, 3]
# dep = [2, 3, 4]
# arr = [ 47, 4, 0, 12, 47, 31, 15, 49, 29, 33, 7, 22, 26, 24, 16 ]
# dep = [ 95, 4, 26, 16, 51, 79, 43, 58, 32, 80, 30, 27, 29, 54, 16 ]
arr = [1, 2, 3, 4 ]
dep = [10, 2, 6, 14 ]
print('Output', hotel(arr, dep, 4))