#include <iostream>

using namespace std;

int main(void)
{
	int N = 0;
	char array = {0,};
	
	cin >> N;
	
	if (N>=1 and N<=100)
	{
		for (int i=1; i<=N; i++) // N��° �� 
		{
			for (int j=1; j<=i; j++) // N���� �� 
			{
				
				cout << "*";
			}
			cout << '\n';
		}
	}
	
	return 0;
}
