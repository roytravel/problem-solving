#include <stdio.h>

int binomial(int n, int k) {
	if (n == k || k == 0)
		return 1;
	else
		return binomial(n - 1, k - 1) + binomial(n - 1, k);
}

int main(void)
{
	int n, k;
	int result;

	scanf_s("%d %d", &n, &k);
	result = binomial(n, k);

	printf("%d\n", result);

	return 0;
}
