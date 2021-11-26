def swap(a, b):
    if a > b:
        a = a-b
        b = a+b
        a = b-a
        print(a)
        print(b)
    else:
        a = b - a
        b = b - a
        a = a+b
        print(a)
        print(b)

swap(10, 20)
swap(78, 16)
swap(55, 55)