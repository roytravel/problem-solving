#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	
	int C = 0; // Test case
	int Sum = 0;
	int Weight = 0;
	string S;
	
	cin >> C;
	
	for (int i=0; i<C; i++)
	{
		cin >> S;
		if (S.length()>0 and S.length()<80)
		{
			for (int j=0; j<S.length(); j++)
			{
				if (S[j] == 'O')
				{
					Weight = Weight + 1;
					Sum = Sum + Weight;
				}
				else
					Weight = 0;
			}
			
			cout << Sum << endl;
			Sum = 0;
			Weight = 0;
		}
		

	}

	return 0;
}
