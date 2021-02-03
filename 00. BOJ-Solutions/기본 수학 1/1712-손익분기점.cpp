#include <iostream>

using namespace std;

int main(void)
{
	int A, B, C = 0;
	int limit = 2100000000;
	
	cin >> A;
	cin >> B;
	cin >> C;
	
	if (A<=limit and A>=1 and B<=limit and B>=1 and C<=limit and C>=1) // initial condition
	{
		if (B>=C)
		{
			cout << -1 << endl;
			return 0;
		}
		
		cout << A/(C-B) + 1;
	}
	
	return 0;
}
