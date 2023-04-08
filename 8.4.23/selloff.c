#include <stdio.h>

int main(){
    int n, f;
    scanf("%d %d", &n, &f);
    int a[10000];
    int profit = 0;
    for (int i = 0; i < n; i++) {
        int k, l;
        scanf("%d %d", &k, &l);
        profit += (k < l) ? k : l;
        a[i] = (2 * k < l) ? (2 * k - k) : (l - k);
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] < a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }}}
    for (int i = 0; i < f; i++) {
        if (i < n) {
            profit += (a[i] > 0) ? a[i] : 0;
        } 
        else {
            break;
        }
    }
    printf("%d\n", profit);

    return 0;
}