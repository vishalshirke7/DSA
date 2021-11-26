"""Basic Euclidean Algorithm for GCD 
The algorithm is based on the below facts. 
If we subtract a smaller number from a larger (we reduce a larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find remainder 0"""


# Python program to demonstrate Basic Euclidean Algorithm
 
 
# Function to return gcd of a and b
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
 
# Code Contributed By Mohit Gupta_OMG <(0_o)>

#TIME COMPLEXITY: O(LOG MIN(A, B))