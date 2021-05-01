from array import *
#
# num = array('d',[1,2,3,4.5,5])
#
# for i in range(5):
#     print(num[i])
#
# print()
# ########################################
# from datetime import datetime
#
# date = datetime.today()
# print(date)
# print()
# #######################################
# #Area of a circle
#
#
# pi=3.14
#
# def circle(r):
#     if r>1:
#         area = pi * (r ** 2)
#         print("The area of a circle is:",area)
#
# circle(2)
# print()
#
# ###########################################
# fname='siva'
# lname='ranjani'
# # fname = input("Enter the first name:")
# # lname = input("enter the last name:")
#
# print("Firstname: {} \nLastname: {}".format(fname,lname))
# print("RFirstname: {} \nRLastname: {}".format(fname[::-1],lname[::-1]))
# print()

############################################

arr = array('i',[])

n = int(input("enter the length of array: "))
for i in range(n):
    x=int(input("enter the elements:"))
    arr.append(x)

print(arr)

#searching for the index value of list
num=int(input("enter the value to be searched:"))
idx = 0

for e in arr:
    if e == num:
        print("Index value of {}:".format(idx))
    idx+=1

#or simple use the function

print(arr.index(num))