#include <stdio.h>
main(short i)
{
    unsigned long int a=0,b=0,c=0,cmp=0;
    scanf("%u %u",&a,&b);
    for (i--,c=a^b;i<32;cmp+=(c>>i)&1,i++);
    printf("\n%.2f%% Compatibility\n%u should avoid %u.\n%u should avoid %u.\n\n",(25*(32-cmp)/8.),a,~a,b,~b);
}