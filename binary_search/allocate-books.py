"""
https://www.interviewbit.com/old/problems/allocate-books/
"""

def numberOfStudents(A, pages):
    count = 0
    students = 1
    for i in range(len(A)):
        count += A[i]
        if count > pages:
            count = A[i]
            students += 1
    return students

def books(A, B):
    if B > len(A):
        return -1
    min_pages = max(A)
    max_pages = sum(A)
    while(min_pages < max_pages):
        mid = int((min_pages + max_pages) / 2)
        if numberOfStudents(A, mid) > B:
            min_pages = mid + 1
        else:
            max_pages = mid
    return min_pages

print(books([12, 34, 67, 90], 2))	