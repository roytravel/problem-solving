#include <iostream>

using namespace std;

int main(void)
{
	
	int N = 0;
	
	cin >> N;
	
	if (N>=1 and N<=100)
	{
		for (int i=1; i<=N; i++) // Count loop
		{
			for (int j=0; j<N-i; j++) // Print loop
			{
				cout << " ";
			}
			
			for (int k=0; k<i; k++)
			{
				cout << "*";
			}
			
			cout << '\n';
		}
	}
	
	return 0;
}
