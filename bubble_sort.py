# arr = [6,2,4,3,1]
# def bubble(arr):
#     for i in range(0, len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr
#
# print(bubble(arr))




def bubble_sort(listt):
    for i, num in enumerate(listt):
        try:
            if listt[i+1] < num:
                listt[i] = listt[i+1]
                listt[i+1] = num
                bubble_sort(listt)
        except IndexError:
            pass
    return listt

listt = [6,2,4,3,1]
print(bubble_sort(listt))