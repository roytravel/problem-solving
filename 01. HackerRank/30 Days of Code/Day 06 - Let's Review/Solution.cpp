#include <iostream>

using namespace std;

int main() 
{
	
	int T;
	string S;
	
	cin >> T;
	
	for (int i=0; i < T; i++)
	{
		cin >> S;
		
		for (int j=0; j < S.length(); j++)
		{
			if (j % 2 == 0)
			{
				cout << S[j];
			}
		}
		
		cout << " ";
		
		for (int j=0; j < S.length(); j++)
		{
			if (j % 2 != 0)
			{
				cout << S[j];
			}
		}
		
		cout << endl;
	}
	return 0;
	
}
