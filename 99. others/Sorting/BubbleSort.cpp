#include <iostream>

using namespace std;

void BubbleSort(int arr[], int n)
{
	int i, j;
	int temp;

	for (i = 0; i < n - 1; i++)
	{
		for (j = 0; j < (n - i) - 1; j++)
		{
			if (arr[j] > arr[j+1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}

}

int main(void)
{
	int i;
	int arr[] = { 5, 2, 7, 3 ,10, 8, 9, 1, 6, 4};

	BubbleSort(arr, sizeof(arr) / sizeof(int));

	for (i = 0; i < sizeof(arr)/sizeof(int); i++)
		cout << arr[i] << " ";

	cout << endl;

	return 0;
}
