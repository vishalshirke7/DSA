# # arr = [3,6,6,7,8]
# # size = len(arr)

# # def reverse(start, arr):
# #     if start >= size - start - 1:
# #         return 
# #     arr[start], arr[size - start - 1] = arr[size - start - 1], arr[start]
# #     reverse(start + 1, arr)

# # reverse(0, arr)
# # print(arr)


# input_str = 'madam'
# size = len(input_str)

# def check_palindrome(start, input_str):
#     if start >= size - start - 1:
#         return True
#     if input_str[start] != input_str[size - start - 1]:
#         return False
#     return check_palindrome(start + 1, input_str)

# (print(check_palindrome(0, input_str)))



def fibonacci_series(n):
    a, b = 0, 1
    if n == 0:
        print(a)
        return 
    if n == 1:
        print(b)
        return
    print(a)
    print(b)  
    for index in range(n - 2):
        c = a + b
        a = b
        b = c
        print(c)  

fibonacci_series(10) 


    BSE, NSE (market where transactions happen)
    |
    |
    V
    RTA             Email/PDF     (Centralized DB)
    Kams, Carvy  ------------>      WealthBoss         <-------- WorkStation (Internal WebApp)
                                        |
                                        |
                                        |
                                        Computation Engine (Number Crunching)
                                            - Calculating Returns - Lambda1 - 1000 - 400 clients
                                            - Capital / Gainloss - Lambda2
                                        |
                                        |
                                        |
                                        V
    Client App  <-----------------------Destination DB (Client Facing Data)
    - API 1 Profile
            1. Caching

    - API 2

Q. Suppose you have 10 boxes and each box contains 10 cricket balls.
9 out of 10 boxes have each cricket balls of 10 gm. Remaining 1 box has each balls of 11 gm. The task is to find the box which contains 11gm balls.


Constraint:
- You have an electronic weighing machine and with the help of that you have to identify the box which contain 11 gm balls.
- You can use the weighing machine only once.


  
number of boxes - 10
number of balls each box - 10

9 boxes will have weight of 100 gms 
1 box will have weight - 110 

b b b b b b b b b b

b b b b b
pull one ball from each box - 101 gm



Input1: "819827313819839123801820380183812838190839810983081293891874871827471897313918390810938091830183989083198290183";
Input2: "81987873827832882392839289329302932302302032093231231231231231231";
Both inputs can be so large that it cannot be directly parsed into any numerical datatype a language has to offer.
You need to write this method: 

SumOfValues(input1 string, input2 string):
    output = "414"
    carry = 1



Q. Write a method which will take an integer input and then prints:
    Fizz if divisible by 3
    Buzz if divisible by 5
    FizzBuzz if divisible by both 3 and 5
    - 



class Solution:

    def countIncreasing(self,arr, n):
        # code here
        ans = 0
        small_index = 0
        for index in range(1, n):
            if arr[index] > arr[index - 1]:
                ans += index - small_index
            else:
                small_index = index
         return ans    