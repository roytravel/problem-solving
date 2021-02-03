#include <stdio.h>

#define NUM 100

int binomial(int n, int k) 
{
	int arr[NUM][NUM];

	if (arr[n][k] > 0) 
		return arr[n][k];

	if ((n == k) || k == 0)
		return 1;

	return arr[n][k] = binomial(n - 1, k - 1) + binomial(n - 1, k);
}

int main() 
{
	int n, k;
	int result;

	scanf_s("%d %d", &n, &k);

	result = binomial(n, k);

	printf("%d\n", result);

	return 0;
}
