n=int(input())
for i in range(n):
    l=int(input())
    a=list(map(int, input().split(' ')))
    count=0
    while(len(a)>0):
        if(len(set(a))==len(a)):
            print(count)
            break
        else:
            a.pop(0)
            count+=1
