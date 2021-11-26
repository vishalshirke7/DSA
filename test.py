# class A:

#     @staticmethod
#     def B():
#         print('B is Called')


# a = A()
# a.B()
# A().B()

def A():
    print('Calling A')
    def B(k):
        print('Calling B')        
        if k==0:
            return 0
        B(k-1)
    B(10)
A()        