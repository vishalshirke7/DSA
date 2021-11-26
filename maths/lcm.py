# def gcd(a,b):
# 	if a == 0:
# 		return b
# 	return gcd(b % a, a)

# def lcm(a,b):
# 	return (a / gcd(a,b))* b

# a = 15
# b = 20
# print('LCM of', a, 'and', b, 'is', lcm(a, b))

# USING Euclidean algorithmsa
# Time Complexity: O(Log min(a, b))

# def power(x, n):
# 	if n==0:
# 		return 1
# 	return x * power(x, n-1)

# print(power(2, 5))


def remainder(number, divisor):
	if number < divisor:
		return number
	while(number >= divisor):
		number -= divisor	
	return number

print(remainder(16,8))