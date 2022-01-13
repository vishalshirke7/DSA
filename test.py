# arr = [3,6,6,7,8]
# size = len(arr)

# def reverse(start, arr):
#     if start >= size - start - 1:
#         return 
#     arr[start], arr[size - start - 1] = arr[size - start - 1], arr[start]
#     reverse(start + 1, arr)

# reverse(0, arr)
# print(arr)


input_str = 'madam'
size = len(input_str)

def check_palindrome(start, input_str):
    if start >= size - start - 1:
        return True
    if input_str[start] != input_str[size - start - 1]:
        return False
    return check_palindrome(start + 1, input_str)

(print(check_palindrome(0, input_str)))
