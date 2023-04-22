a= [3,4,1,3]
count=0
n=(int(len(a)))
for i in range(0,n):
    for j in range(i,n):
        if (a[i]==a[j]):
            a.pop(i)
            i=i-1
            count+=1
        
print(count)
# for i in range(0,int(len(a))):
#     if(int(a[i]) in a):
#         a.pop(i)
# print(len(a))