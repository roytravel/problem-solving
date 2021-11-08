#include <iostream>
#include <stdio.h>

using namespace std;

// A에서 X보다 작은 수를 출력하는 프로그램 작성 

int main(void)
{
	// 수열 A를 이루는 정수 N개 
	int N = 0;
	
	// 정수 X 
	int X = 0;
	
	scanf("%d %d", &N, &X);
	
	do
	{
		cin >> N;
//		cout << N << endl;
	} while (getc(stdin) == ' ');
	
	return 0;
	
//	scanf("%d %d", &N, &X);
//	
//	if (N>=1 and ((X<=10000) and (X>=1)))
//	{
//		scanf("")
//	}
}
