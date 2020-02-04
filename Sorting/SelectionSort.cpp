#include <iostream>

using namespace std;

void SelSort(int arr[], int n)
{
	int i, j;
	int maxIdx;
	int temp;

	for (i = 0; i < n - 1; i++)
	{
		maxIdx = i;

		for (j = i + 1; j < n; j++)
		{
			if (arr[j] < arr[maxIdx])
				maxIdx = j;
		}

		temp = arr[i];
		arr[i] = arr[maxIdx];
		arr[maxIdx] = temp;

	}
}


int main(void)
{
	int arr[] = { 5, 2, 7, 3 ,10, 8, 9, 1, 6, 4};
	int i;

	SelSort(arr, sizeof(arr) / sizeof(int));

	for (i = 0; i < sizeof(arr)/sizeof(int); i++)
		cout << arr[i] << " ";

	cout << endl;
	return 0;
}
