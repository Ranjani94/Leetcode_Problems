arr = [6,2,4,3,1]

def insert(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j>= 0 and temp <arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp

    return arr

print(insert(arr))