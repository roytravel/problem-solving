using namespace std;
#include <iostream>

void MergeTwoArea(int arr[], int left, int mid, int right)
{
	int fIdx = left;
	int rIdx = mid + 1;
	int i;

	int * sortArr = (int*)malloc(sizeof(int)*(right + 1));
	int sIdx = left;

	while (fIdx <= mid && rIdx <= right)
	{
		if (arr[fIdx] <= arr[rIdx])
			sortArr[sIdx] = arr[fIdx++];
		else
			sortArr[sIdx] = arr[rIdx++];
		
		sIdx++;
	}

	if (fIdx > mid)
	{
		for (i = rIdx; i <= right; i++, sIdx++)
			sortArr[sIdx] = arr[i];
	}

	else
	{
		for (i = fIdx; i <= mid; i++, sIdx++)
			sortArr[sIdx] = arr[i];
	}

	for (i = left; i <= right; i++)
		arr[i] = sortArr[i];

	free(sortArr);
}


void MergeSort(int arr[], int left, int right)
{
	int mid;

	if (left < right)
	{
		//중간 지점 계산
		mid = (left + right) / 2;

		//둘로 나눠 각각 정려
		MergeSort(arr, left, mid);
		MergeSort(arr, mid + 1, right);

		// 정렬된 두 배열 병합
		MergeTwoArea(arr, left, mid, right);
	}
}


int main(void)
{
	int arr[7] = { 3, 2, 4, 1, 7, 6 ,5 };
	int i;

	//배열 arr의 전체 영역 정렬
	MergeSort(arr, 0, sizeof(arr) / sizeof(int) - 1);

	for (i = 0; i < 7; i++)
		cout << arr[i] << " ";

	cout << endl;
	return 0;
}
