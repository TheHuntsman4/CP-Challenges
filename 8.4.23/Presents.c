

// https://codeforces.com/contest/136/problem/A

#include <stdio.h>
int main()
{
int n,pi;
scanf("%d",&n);
int A[n];
for(int i=1;i<n+1;i++){
    scanf("%d",&pi);
    A[pi-1]=i;
}
for(int i=0;i<n;i++){
    printf("%d ",A[i]);
}

    return 0;
}
