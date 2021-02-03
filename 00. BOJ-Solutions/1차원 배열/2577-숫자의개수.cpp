#include <iostream>

#define NUM 10
using namespace std;

//int getDigitCount(int Value)
//{
//	int count = 0;
//	
//	
//	while (true)
//	{
//		Value = Value / 10;
//		count = count + 1;
//		
//		if (Value == 0)
//		{
//			break;
//		}
//	}
//	
//	return count;
//}

int main(void)
{
	int A, B, C = 0;
	int sum = 0;
	int count = 0;
	
	cin >> A >> B >> C;
	
	if (A>=100 and A<1000 and B>=100 and B<1000 and C>=100 and C<1000) 
	{
		sum = A * B * C;
//		count = getDigitCount(sum);
		int Array[NUM] = {0,};
		
		while (sum!=0)
		{
			Array[sum % 10] = Array[sum % 10] + 1;
			sum = sum / 10;
		}
		
		
		for (int j=0; j<NUM; j++) // Loop for printing the count of each digit.
		{
			cout << Array[j] << endl;
		}
		
	}
	
	return 0;
}
