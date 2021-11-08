#include <iostream>

#define N 10001
using namespace std;

int solution(int n)
{
	int sum = n;
	
	while(true)
	{
		if (n==0)
			break;
		
		sum = sum + (n % 10); // get the remainder
		n = n / 10; // divide by 10 to get next remainder;
	}
	
	return sum;
}


int main(void)
{
	bool Array[N] = {0, };
	int idx = 0;
	
	for (int i=1; i<N; i++)
	{
		idx = solution(i);
		
		if (idx <= N) // Why always idx is smaller or equal than N?
			Array[idx] = 1; // constructor = 1
	}
	
	for (int j=1; j<N; j++)
	{
		if (!Array[j])
			cout << j << endl;
	}
	
	return 0;
}
