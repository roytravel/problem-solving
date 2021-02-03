#include <iostream>

using namespace std;

int main(void)
{
	int N = 0;
	int Max = 0;
	int Min = 0;
	
	cin >> N;
	
	if (N>=1 and N<=1000000)
	{
		int Array[N] = {0,};
		
		for (int i=0; i<N; i++) // ют╥б loop 
		{
			cin >> Array[i];
		}
		
		Max = Array[0];
		Min = Array[0];
		
		for (int j=0; j<N; j++) // Loop for finding Max
		{
			if (Array[j] >= Max)
			{
				Max = Array[j];
			}
		}
		
		for (int k=0; k<N; k++) // Loop for finding Min
		{
			if (Min >= Array[k])
			{
				Min = Array[k];
			}
		}
		
	}
	
	cout << Min << ' ' << Max << endl;
	
	return 0;
}
