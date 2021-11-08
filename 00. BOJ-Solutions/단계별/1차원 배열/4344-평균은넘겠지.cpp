#include <iostream>
#include <math.h>

using namespace std;

int main(void)
{
	
	int C = 0;
	int N = 0;
	
	cin >> C;
	
	for (int i=0; i<C; i++) // This loop means the number of test case.
	{
		cin >> N;
		
		if (N>=1 and N<=1000)
		{
			int Sum = 0;
			double Mean = 0;
			double count = 0;
			double percent = 0;
			
			int Score[N] = {0, };
			
			for (int j=0; j<N; j++) // This loop gets the summation of input values
			{
				cin >> Score[j];
				if (Score[j]< 0 or Score[j]>100)
					return 0;
					
				Sum = Sum + Score[j];
			}
			
			Mean = Sum / N;
			
			for (int k=0; k<N; k++) // This loop gets count of people who has higher value than mean
			{
				if (Score[k] > Mean)
				{
					count = count + 1;
				}
			}
			
		
			percent = (count/N) * 100;
			cout << fixed;
			cout.precision(3);
			cout << round(percent * 1000) / 1000 << "%" << endl;
		}
		
	}

	return 0;
}
