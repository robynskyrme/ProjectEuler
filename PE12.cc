
#include <stdio.h>
#include <math.h>

// 17.2.2024, first Project Euler in C

int main() {
    int n = 1;
    int t = 2;
    
    int factors = 0;
    
    int found = 0;
    
    while (found == 0) {
        factors = 0;
        t = n * (n+1)/2;
        
        int i;
        for (i = 1; i <= (int)sqrt(t)+1; i++) {
            if (t % i == 0) {
                factors +=2;
            }
        }
        
        n++;
        
        if (factors > 499) {
            found = 1;
        }
    }

    printf("%d",t);
    printf("\ndone\n");

    return 0;
}
