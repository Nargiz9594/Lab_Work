# с помощью цикла
n = int(input())

f=1

while n>1:
    f =f*n
    n=n-1
    print(f)


    # с помощью рекурския

    n = int(input())

    f = 1

    for i in range(2, n + 1):
        f = f * i

        print(f)