#include <iostream>

using namespace std;

int main(void)
{
	int N = 0;
	
	cin >> N;
	
	if (N>=1 and N<=100000)	
	{
		for (int i=N; i>0; i--)
		{
			cout << i << '\n';
		}
	}
}
