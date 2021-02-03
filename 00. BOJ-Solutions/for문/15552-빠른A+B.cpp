#include <iostream>

using namespace std;

int main(void)
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int T = 0;
	int A = 0;
	int B = 0;
	
	cin >> T;
	
	if (T<=1000000)
	{
		for (int i=0; i<T; i++)
		{
			cin >> A >> B;	
			if ((A>=1 and A<=1000) and (B>=1) and (B<=1000))
			{
				cout << A+B << '\n';	
			}
		}
	}
	
	return 0;
}
