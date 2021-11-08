#include <stdio.h>

int main(void)
{
	int N = 0;
	
	scanf("%d", &N);
	
	if (N >= 1 and N <= 9)
	{
		for (int i=1; i<=9; i++)
		{
			printf("%d * %d = %d\n", N, i, N*i);
		}
	}
	
	else
		return 0;
		
	return 0;
}
