def fibonacci_series(a, b, limit):
    print(a)
    print(b)
    a = a+b
    if a < limit and b <limit:
        fibonacci_series(a ,a + b, limit)
    return 

fibonacci_series(0, 1, 10)    


# USING DP

def n_fibonacci(n):
    l1 = [0, 1]
    for i in range(2, n + 1):
        l1.append(l1[i-1] + l1[i-2])
    return l1[n]

output = n_fibonacci(9)
print(output)

# TIME COMPLEXITY - O(n)


# Function for nth Fibonacci number

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(9))

# TIME COMPLEXITY - EXPONENTIAL T(n) = T(n-1) + T(n-2) --> 2^n
