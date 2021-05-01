#
# li = [1,2,3,4,5,6,7,8,9]
#
# def odd_even(lis):
#     for i in lis:
#         if i % 2 ==0:
#             print("Even number",i)
#         else:
#             print("Odd number",i)
#
#
# odd_even(li)


####################################

#count of list

# num = [1,2,3,4,5,6,7,8,9,10]
#
#
# def count(l):
#     even=0
#     odd=0
#
#     for i in l:
#         if i % 2 == 0:
#             even+=1
#         else:
#             odd+=1
#
#     return even,odd
#
#
# even,odd =count(num)
# print("No of even: {} and no of odd: {}".format(even,odd))



#####################################
def li():
    num = int(input("Enter the number of names:"))
    name = []
    for i in range(num):
        add = input("enter the name:")
        name.append(add)
    print("Names in list:",name)

    #
    # for i, v in enumerate(name):
    #     if len(v) > 5:
    #         print("Names which greater than 5 letters:",i,v)

    for i in range(len(name)):
        if len(name[i])>5:
            print("Index : {} and Value: {}".format(i,name[i]))
li()

# x='siva'
# count=len(x)
# print(count)
