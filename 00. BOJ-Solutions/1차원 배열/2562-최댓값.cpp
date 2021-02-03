#include <iostream>

#define NUM 9
using namespace std;

int main(void)
{
	int Array[NUM] = {0,};
	int Max = 0;
	int Order = 0;
	
	for (int i=0; i<NUM; i++) // loop for input
	{
		cin >> Array[i];
	}
	
	for (int j=0; j<NUM; j++) // loop for checking boundary
	{
		if (Array[j] > 100)
		{
			return 0;
		}
	}
	
	for (int k=0; k<NUM; k++)
	{
		if (Array[k] >= Max)
		{
			Max = Array[k];
			Order = k+1;
		}
	}
	
	cout << Max << endl;
	cout << Order << endl;
	
	return 0;
}
