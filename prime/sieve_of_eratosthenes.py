import math

# def sieve_of_eratosthenes(input_number):
#     current_index = 2
#     prime_numbers = list()
#     numbers_flag = [True for i in range(input_number + 1)]
#     while (current_index * current_index <= input_number):
#         if (numbers_flag[current_index] is True):
#             for i in range(current_index * current_index, input_number + 1, current_index):
#                 numbers_flag[i] = False
#         current_index += 1
#     for i in range(2, input_number+1):
#         if numbers_flag[i] is True:
#             prime_numbers.append(i)
#     return prime_numbers


# prime_numbers = sieve_of_eratosthenes(100)
# print(prime_numbers)


def sieve_of_eratosthenes_1(n):
    prime_number = 2
    all_numbers = [True for i in range(n)]
    while(prime_number <= int(math.sqrt(n))):
        cross_of(prime_number, all_numbers)
        prime_number = get_next_prime(prime_number, all_numbers)
    for i in range(2, len(all_numbers)):
        if all_numbers[i] is True:
            print(i)

def cross_of(prime_number, all_numbers):
    for index in range(prime_number*prime_number, len(all_numbers), prime_number):
        all_numbers[index] = False

def get_next_prime(prime_number, all_numbers):
    for i in range(prime_number + 1, len(all_numbers)):
        if all_numbers[i] is True:
            return i 


sieve_of_eratosthenes_1(50)