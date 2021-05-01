# def fizz(n):
#     l = []
#     for i in range(1,n+1):
#         if i%3 == 0 and i%5 == 0:
#             l.append('FizzBuzz')
#         elif i%3 == 0:
#             l.append('Fizz')
#         elif i%5 == 0:
#             l.append('Buzz')
#         else:
#             l.append(str(i))
#     print(l)

def fizz(n):
    li = []
    dict = {3: 'Fizz', 5: 'Buzz'}
    for num in range(1, n + 1):
        stra = ""
        for key in dict.keys():
            if num % key == 0:
                stra += dict[key]
        if not stra:
            stra = str(num)

        li.append(stra)
    return li

li = fizz(15)
print(li)