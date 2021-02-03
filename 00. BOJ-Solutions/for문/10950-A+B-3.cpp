#include <stdio.h>

int main(void)
{
	int T = 0;
	int A = 0;
	int B = 0;
	
	scanf("%d\n", &T);
	
	for (int i=0; i<T; i++)
	{
		scanf("%d %d", &A, &B);
		if (A > 0 and B < 10)
		{
			printf("%d\n", A+B);
		}
	}
	
	return 0;
}
