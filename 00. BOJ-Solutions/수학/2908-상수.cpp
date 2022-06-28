#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void)
{
	string a, b;
	cin >> a >> b;
	if (a.size() == 3 and b.size() == 3)
	{
		reverse(a.begin(), a.end());
		reverse(b.begin(), b.end());
		if (a > b)
			cout << a;
		else
			cout << b;
	}
	return 0;
}