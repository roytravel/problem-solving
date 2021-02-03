#include <iostream>

using namespace std;

int main(void)
{
	
	int n = 0;
	int sum = 0;
	int prime = 0;

	while(true)
	{
		cin >> n;
		
		if (n>=1 and n<=123456)
		{			
			for (int i=n; i<=n*2; i++)
			{
				
				for (int j=1; j<=i; j++)
				{
					if (i % j == 0)
						sum = sum + 1;	
				}
				
				if (sum == 2)
					prime = prime + 1;
				
				sum = 0;
			
			}
			cout << prime << endl;
			prime = 0;
		}
		
		else
			break;
	}
	return 0;
}
