"""This property can be proved using counter statement.
Let a and b be two factors of n such that a*b = n.
If both are greater than sqrt(n), then a.b > sqrt(n), * sqrt(n), which contradicts the expression a * b = n."""

import math
def find_factors(n):
    output = list()
    even_mod = 2
    while((n % even_mod) == 0):
        output.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while(n%i==0):
            output.append(i)
            n //= i
    if n > 2:
        output.append(n)
    return output

print(find_factors(500))
