#RECURSIVE METHOD
def fact(n):
    if n==0:
        return 1
    elif n<0:
        return "Enter valid number"
    else:
        return n * fact(n-1)

print(fact(10))


def factorial(n):
    num=1
    if n==0:
        return 1
    for i in range(1,n+1):
        num = num * i

    print(num)

factorial(5)
