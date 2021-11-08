#include <iostream>
#include <vector>
using namespace std;


long long sum(vector<int> &a) // Solution 1
{
	long long ans = 0;
	
	for(vector<int>::iterator i = a.begin(); i<a.end(); i++)
	{
		ans = ans + *i;
	}
	
	return ans;
}


//long long sum(vector<int> &a) // Solution 2
//{
//	long long Sum = 0;
//	for(auto aa: a)
//	{
//		Sum = Sum + aa;
//	}
//	
//	return Sum;
//}



//int getSum(int a[], int l) // Solution 3
//{
//	int Sum = 0;
//	
//	for (int i=0; i<l); i++)
//	{
//		if (a[i] >=0 and a[i]<=1000000)
//		{
//			Sum = Sum + a[i];
//		}
//		
//		else
//			return 0;
//	}
//	
//	return Sum;
//}
//
//int main(void)
//{
//	
//	int n = 0;
//	
//	cin >> n;
//	
//	if (n>=1 and n<=300000)
//	{
//		int a[n] = {0,};
//		
//		for (int i=0; i<n; i++)
//		{
//			cin >> a[i];
//		}
//		
//		int Sum = getSum(a, sizeof(a)/sizeof(int));
//		
//		cout << Sum << endl;
//	}
//	
//	return 0;
//}
