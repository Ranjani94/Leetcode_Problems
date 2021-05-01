#Prime number
Lower = int(input("Enter the lower range:"))
Upper = int(input("Enter the Upper range:"))
a = "hppy"

for num in range(Lower, Upper+1):
    #if num>1:
    print(num)
    for i in range(2,num):
        print(i)
        if num % i == 0:
            break
    else:
        print(num)


