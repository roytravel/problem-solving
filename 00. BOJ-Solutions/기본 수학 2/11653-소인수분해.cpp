#include <iostream>

using namespace std;

int main(void)
{
	
	int N = 0;
	int i = 2;
	
	cin >> N;
	
	if (N>=1 and N<=10000000)
	{
		while (true)
		{
			if(N % i == 0) // 72 % 2 == 0, 
			{
				cout << i << endl; // 2 
				N = N / i; // 36 = 72 / 2
				i = 1; 
			}	
			i = i + 1;
			
			if (N==1)
			{
				break;
			}
		}
	}
	
	return 0;
	
}
