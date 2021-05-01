li = [3,5,6,7,9,6]

n=9

pos= 0


def lin_search(l,num):
    for i in range(len(l)):
        if l[i] == num:
            globals()['pos'] = i
            return True
    else:
        return False




if lin_search(li, n):
    print("Found",n , 'at position',pos)
else:
    print('not found')