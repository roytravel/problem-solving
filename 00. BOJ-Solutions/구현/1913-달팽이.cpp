#include <iostream>
#include <cstring>

using namespace std;

int main(void)
{
	// 1. 변수 선언부
	int N = 0; // 입력 받을 홀수 자연수
	int want = 0; // N^2 이하의 찾고자 하는 자연수
	int x = 0, y = 0 ; // Want의 좌표를 나타낼 x, y 값
	int row = -1, col = 0;; // 달팽이를 나타낼 행, 열
	int dir = 1; // 방향을 나타낼 변수
	cin >> N;
	int copy = N;
	cin >> want;
	int squared = N * N; // N^2을 표현할 변수

	int** arr;
	arr = new int* [N]; // 2차원 배열의에서 사용할 배열의 길이(row)

	for (int i = 0; i < N; i++)
	{
		arr[i] = new int[N]; // N = 2차원 배열에서 사용할 배열의 길이(column)
		memset(arr[i], 0, sizeof(int)*N); // 0으로 배열 초기화 for security.
	}


	// 2. 핵심 알고리즘 동작부
	while (squared > 0)
	{
		for (int i = 0; i < copy; i++)
		{
			row = row + dir;
			arr[row][col] = squared;
			if (squared == want)
			{
				x = row + 1;
				y = col + 1;
			}
			squared = squared - 1;
		}

		copy = copy - 1;
		for (int i = 0; i < copy; i++)
		{
			col = col + dir;
			arr[row][col] = squared;
			if (squared == want)
			{
				x = row + 1;
				y = col + 1;
			}
			squared = squared - 1;
		}
		dir = dir * (-1);
	}

	// 3. 결과 출력부
	for (int i = 0; i < N * N; i++)
	{
		int r = i / N;
		int c = i % N;
		cout << arr[r][c] << " ";
		if ((i % N) == N - 1) cout << endl;
	}

	cout << x << " " << y << endl;


	// 4. 2차원 배열 할당 해제부
	for (int i = 0; i < N; i++)
		delete[] arr[i];
	delete[] arr;

	return 0;
}