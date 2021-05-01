#Addition of first 10 fibonacci numbers

def fib(n):
    # a=0
    # b=1
    if n<=0:
        print("enter valid number")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:

        return fib(n-1) + fib(n-2)




    #
    # for i in range(2,n):
    #     c=a+b
    #     if c < 100:
    #         print("The value of a:{} and b:{} is equal to c:{}".format(a, b, c))
    #     a=b
    #     b=c



        #print("The value of c:", c)


        #print("value of a: {}  b: {}  c: {}".format(a,b,c))
print(fib(10))
