#include <iostream>

#define BIG 5
#define SMALL 3

using namespace std;

int Solution(int N)
{
	int quoteB = N / BIG; // ū ������ upper bound�� �켱 ����
	
	while(true)
	{
		
		int Remainder = N - (BIG * quoteB); // ū ������ ������ ���� ������ ���� 
		if (Remainder % SMALL == 0)	// �������� ���� �������� �� ������ ��� ū ���� ���� + ���� ���� ���� ��ȯ 
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
