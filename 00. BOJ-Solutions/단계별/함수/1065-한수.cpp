#include <iostream>

using namespace std;


bool hansoo(int i)
{
	if (i < 100)
		return true;
		
	int a = i / 100;
	int b = i / 10 % 10;
	int c = i % 10;
	
	if (a+c == 2*b)
	{
		return true;
	}
	
	return false;
}


int main(void)
{
	
	int N = 0;
	int count = 0;
	
	cin >> N;
	
	if (N>=1 and N<=1000) // Initial condition
	{
		
		for (int i=1; i<=N; i++)
		{
			if(hansoo(i))
				count = count + 1;
		}
		
		cout << count << endl;
	}
	
	return 0;
}
