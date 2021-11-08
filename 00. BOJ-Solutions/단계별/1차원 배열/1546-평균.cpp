#include <iostream>

using namespace std;

int main(void)
{
	int N = 0;
	int Max = 0;
	long double Sum = 0;
	
	
	cin >> N;
	
	if (N>0 and N<=1000)
	{
		long double Score[N] = {0,};
		
		for (int i=0; i<N; i++)
		{
			cin >> Score[i];
			if (Score[i]>=Max)
			{
				Max = Score[i];
			}
		}
		
		for (int j=0; j<N; j++)
		{
			Score[j] = (Score[j] / Max) * 100;
			Sum = Sum + Score[j];
		}
		
		cout << Sum/N << endl;
	}
	
	return 0;
}
