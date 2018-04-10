#include <stdio.h>

#define N 100000

int main(void)
{
    size_t sum[N+1];
    int halfN=N/2+1;
    for(size_t i=0;i<=N;i++)
        sum[i]=1;

    for(size_t i=2;i<=halfN;i++)
    {
        for(size_t j=i<<1;j<=N;j+=i)
        {
            sum[j]+=i;
        }
    }

    for(size_t i=0;i<=N;i++)
    {
        if(sum[i]<=N && sum[sum[i]]==i && sum[i]>i)
            printf("%d    %d\n",i,sum[i]);
    }

    return 0;
}