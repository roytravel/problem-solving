#include <iostream>

using namespace std;

int main(void)
{
	int T = 0;
	int A = 0;
	int B = 0;
	
	cin >> T;
	
	for (int i=0; i<T; i++)
	{
		cin >> A >> B;
		if (A>0 and B<10)
		{
			cout << "Case #" << i+1 << ": " << A << " + " << B << " = " << A+B << endl;
		}
	}
	
	return 0;
}
