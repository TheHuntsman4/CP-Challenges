n=int(input())
body=[]
x,y,z=0,0,0
for i in range(n):
    force=list(map(int, input().split(' ')))
    body.append(force)
for i in range(len(body)):
    x+=body[i][0]
    y+=body[i][1]
    z+=body[i][2]
if(x==y==z==0):
    print("YES")
else:
    print("NO")