#include <iostream>
#include <map>

using namespace std;

int main()
{
	
	int n = 0;
	cin >> n;
	
	map <string, int> phone_book;
	string name;
		
	
	for (int i = 0; i< n; i++)
	{
		cin >> name;
		
		if (!phone_book[name])
		{
			cin >> phone_book[name];
		}
	}
	
	
	while(cin >> name)
	{	
		if (phone_book[name])
		{
			cout << name << "=" << phone_book[name] << endl;
		}
		
		else
		{
			cout << "Not found" << endl;
		}
		
		n = n - 1;
	}
	
	return 0;
}
