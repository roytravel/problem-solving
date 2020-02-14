#include <iostream> 
#define SIZE 1000 
using namespace std; 

long long array[SIZE] = { 0, 1, 1, };

long long fibonacci(int num) 
{ 
	if (array[num])
		return array[num];

	else
		return array[num] = fibonacci(num - 1) + fibonacci(num - 2);
	
} 

int main() 
{ 
	int n; 
	cin >> n;
	
	cout << fibo(n) << endl; 
	
	return 0;	
}
