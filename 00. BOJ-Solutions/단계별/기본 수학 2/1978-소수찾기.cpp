#include <iostream>

using namespace std;

int main(void)
{
	int N = 0;
	int num = 0;
	int count = 0;
	int sum = 0;
	
	cin >> N;
	
	if (N<=100) // initial condition
	{
		for (int i=0; i<N; i++)
		{
			cin >> num;
			
			if (num<=1000)
			{
				for (int j=1; j<=num; j++)
				{
					if (num % j == 0)
					{
						count = count + 1;
					}
				}
				
				if (count == 2)
					sum = sum + 1;
					count = 0;
			}
		}
		
		cout << sum << endl;
	}
	
	
	return 0;
}
