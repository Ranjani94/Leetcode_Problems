li = [4,6,4,2478,78,789,6578,35]
n = 7

def bin_search(li,n):
    li.sort()
    print(li)
    l = 0
    u = len(li)-1
    #exit()
    while l <= u:
        mid = (l+u) // 2
        print(l,u,mid)
        if li[mid] == n:
            return True
        else:
            if li[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

if bin_search(li,n):
    print("found", n)
else:
    print("not found")

