from functools import reduce

num = [1,2,3,4,5,6,7,8,9,10]

#Fiilter
even = list(filter(lambda n : n%2==0,num))
#Map
map = list(map(lambda n : n*2, even))
#reduce
red = reduce(lambda a,b: a/b,map)

print(red)