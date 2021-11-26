def findNumbers(nums):
    count = 0
    for number in nums:
        quotient = (number // 10)
        quotient_digit_count = 1 if quotient is 0 else (len(str(quotient)) + 1)
        if (quotient_digit_count % 2) == 0:
            count += 1
    return count

print(findNumbers([12,345,2,6,7896]))
