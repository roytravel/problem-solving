#include <iostream>

using namespace std;

int main(void)
{
	int M = 0;
	int N = 0;
	
	int Count = 0;
	int Min = 0;
	int Sum = 0;
	int flag = true;

	cin >> M;
	cin >> N;
	
	
	if (M<=10000 and M>=1 and N<=10000 and N>=1) // initial condition
	{	
		for (int i=M; i<=N; i++) // M이상 N이하 자연수  
		{
			for (int j=1; j<=i; j++) // M까지의 수 
			{
				if (i % j == 0) // 소수 확인을 위해 M을 j로 나누어 Count를 계산 
				{
					Count = Count + 1;		 
				}
			}
			
			
			if (Count == 2) // 나누어지는게 1과 자기 자신 밖에 없는 소수라면 
			{
				Sum = Sum + i;
				
				if (flag)
				{
					Min = i;
					flag = false;	
				}
				
			}
			Count = 0;
		}
		
		
		if (Sum == 0)
		{
			cout << -1 << endl;
			return 0;
		}
		
		cout << Sum << endl;
		cout << Min << endl;
	}
	
	return 0;
}
