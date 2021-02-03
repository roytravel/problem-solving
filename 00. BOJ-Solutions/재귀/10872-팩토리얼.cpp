#include <iostream>

using namespace std;

int factorial(int N)
{	
	if (N<=1)
		return 1;
		
	return (N * factorial(N-1));	
}


int main(void)
{
	
	int N = 0;
	int result = 0;
	
	cin >> N;
	
	if (N>=0 and N<=12)
	{
		result = factorial(N);
		cout << result << endl;
	}
	
	return 0;
}
