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
		for (int i=M; i<=N; i++) // M�̻� N���� �ڿ���  
		{
			for (int j=1; j<=i; j++) // M������ �� 
			{
				if (i % j == 0) // �Ҽ� Ȯ���� ���� M�� j�� ������ Count�� ��� 
				{
					Count = Count + 1;		 
				}
			}
			
			
			if (Count == 2) // ���������°� 1�� �ڱ� �ڽ� �ۿ� ���� �Ҽ���� 
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
