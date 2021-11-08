#include <iostream>

#define NUM 42
using namespace std;

int main(void)
{
	int Input[10] = {0,};
	int Remainder[10] = {0,};
	int count = 0;
	
	for (int i=0; i<10; i++) // Loop for input digit to array
	{
		cin >> Input[i];
		if (Input[i]<0 and Input[i]>1000)
		{
			return 0;
		}
	}
	
	
	for (int j=0; j<10; j++) // Loop for Assigning reaminder to array varaible -> Remainder
	{
		Remainder[Input[j] % NUM -1] = Remainder[Input[j] % NUM -1] + 1;
	}
	
	for (int k=0; k<10; k++) // Loop for checking is there digit except 0
	{
		
		if (Remainder[k] != 0)
		{
			count = count +1;
		}
		
		else
		{
			for (int l = 0; l<10; l++) // Loop for checking if all things in Reaminder is zero. if so, assign 1 to count.
			{
				if (Remainder[l])
				{
					break;	
				}
				
				else
				{
					count = 1;
				}
				
			}	
		}
		
	}
	
	cout << count << endl;
	
	return 0;
}
