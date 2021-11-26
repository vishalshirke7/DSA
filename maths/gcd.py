def calculate_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return calculate_gcd(a-b, b)
    return calculate_gcd(a, b-a)

gcd = calculate_gcd(5, 25)
print(gcd)

# USING Euclidean algorithms

"""
Basic Euclidean Algorithm for GCD 
The algorithm is based on the below facts. 

If we subtract a smaller number from a larger (we reduce a larger number), GCD does not change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find remainder 0.
"""


def gcd(a, b): 
    if a == 0 :
        return b      
    return gcd(b%a, a)
 
a = 10
b = 15
print("gcd(", a , "," , b, ") = ", gcd(a, b))
 
a = 35
b = 10
print("gcd(", a , "," , b, ") = ", gcd(a, b))
 
a = 31
b = 2
print("gcd(", a , "," , b, ") = ", gcd(a, b))