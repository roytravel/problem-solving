#include <iostream>

using namespace std;

int main(void)
{
	int N = 0;
	int count = 0;
	int quote = 0;
	int remain = 0;
	int sum = 0;
	int newNumber = 0;
	int tempN = 0;
	
	cin >> N;
	
	if (N>=0 and N<=99)
	{
		
		tempN = N;
		
		
		while  (true)
		{
			quote = tempN / 10; //2, 6, 8, 4
			remain = tempN % 10; // 6, 8, 4, 2
			sum = quote + remain; // 8, 14, 12, 6
			
			if (sum <10)
			{
				sum = (sum * 10) + sum;
			}
			
			tempN = (remain * 10) + (sum % 10); // 8, 84, 42, 2
			count = count + 1; // 1, 2, 3, 4
			
			if (N == tempN)
			{
				cout << count << '\n';
				break;
			}	
		}

	}
	
	return 0;
}
