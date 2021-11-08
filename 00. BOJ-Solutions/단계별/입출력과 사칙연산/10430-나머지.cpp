#include <stdio.h>

int main(void)
{
	int A, B, C = 0;
	
	scanf("%d %d %d", &A, &B, &C);
	
	if (A>=2 and B>=2 and C>=2)
	{
		if (A<=10000 and B<= 10000 and C<= 10000)
		{
			printf("%d\n", (A+B)%C);
			printf("%d\n", ((A%C) + (B%C))%C);
			printf("%d\n", (A*B)%C);
			printf("%d\n", ((A%C)*(B%C))%C);
		}
	}
	
	return 0;
}
