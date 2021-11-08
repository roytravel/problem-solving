#include <iostream>

#define BIG 5
#define SMALL 3

using namespace std;

int Solution(int N)
{
	int quoteB = N / BIG; // 큰 설탕의 upper bound를 우선 결정
	
	while(true)
	{
		
		int Remainder = N - (BIG * quoteB); // 큰 설탕의 개수에 따라 나머지 결정 
		if (Remainder % SMALL == 0)	// 나머지가 작은 설탕으로 딱 떨어질 경우 큰 설탕 개수 + 작은 설탕 개수 반환 
		{
			int quoteS = Remainder / SMALL;
			return quoteB+quoteS;
		}
		
		if (quoteB == 0)
			break;
			
		quoteB = quoteB -1;
	}
	
	return -1;
	
}

int main(void)
{
	int N = 0;
	
	cin >> N;
	
	if (N>=3 and N<=5000)
	{
		int result = Solution(N);
		cout << result;
	}
	
	return 0;
}
