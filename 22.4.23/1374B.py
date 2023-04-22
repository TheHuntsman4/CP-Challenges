i=int(input())
for x in range(i):
    n = int(input())
    if n == 1:
        print(0)
        continue
    div2, div3 = 0, 0
    while n % 2 == 0:
        div2 += 1
        n //= 2
    while n % 3 == 0:
        div3 += 1
        n //= 3
    if (div3 >= div2 and n == 1):
        print(2 * div3 - div2)
    else:
        print(-1)
    