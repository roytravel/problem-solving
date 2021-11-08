#include <stdio.h>

int main(void)
{
	int A = 0;
	int B = 0;
	
	scanf("%d %d", &A, &B);
	
	if (A < 1 or ((B > 10000) and (B <= 0)))
		return 0;
	
	printf("%d\n", A+B);
	printf("%d\n", A-B);
	printf("%d\n", A*B);
	printf("%d\n", A/B);
	printf("%d\n", A%B);
	
	return 0;
}
