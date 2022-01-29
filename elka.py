print("ведите значение от 1 до 9")
n = int(input())
k = str()
u = n
if n <= 9 and n > 0:
    for i in range(1,n+1):
        o = ''.join(reversed(k))
        k = k + str(i)
        u = u - 1
        for j in range(u):
            print(' ', end='')
        print(k + o)
else:
    print('введено неверное значение')