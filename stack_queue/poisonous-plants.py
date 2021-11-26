"""
https://www.hackerrank.com/challenges/poisonous-plants/problem
"""

def poisonousPlants(p):
    days = 0
    while True:
        index, died = len(p) - 1, False
        while index > 0:
            while p[index] is None:
                index -= 1
            if index <= 0:
                break
            temp = index - 1
            while p[temp] is None:
                temp -= 1
            if temp <= 0:
                break
            if p[temp] < p[index]:
                p[index] = None
                died = True
            index = temp
        if not died:
            break
        else:
            days += 1
    return days


print('Output', poisonousPlants())    