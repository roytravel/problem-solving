#include <iostream> 
#define SIZE 1000 
using namespace std; 

long long array[SIZE] = { 0, 1, 1, };

long long fibonacci(int num) 
{
	
	if (num == 0)
		return 0;

	if (num == 1 || num == 2)
		return 1;

	if (array[num])
		return array[num];

	else
		return array[num] = fibonacci(num - 1) + fibonacci(num - 2);
	
} 

int main() 
{ 
	int n; 
	cin >> n;
	
	cout << fibonacci(n) << endl; 
	
	return 0;	
}
