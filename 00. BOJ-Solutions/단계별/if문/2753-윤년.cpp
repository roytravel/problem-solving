#include <iostream>

using namespace std;

bool checkLeapYear(int year)
{
	if ((year % 4 == 0 and year % 100 != 0) or (year % 4 ==0 and year % 400 == 0))
	{
		return true;
	}
	
	else
	{
		return false;
	}
}

int main(void)
{
	int result = -1; // ���� Ȯ�� 
	int year = 0; // �Է� ���� 

	cin >> year;
	
	if (year>=1 and year<=4000)
	{
		result = checkLeapYear(year);
		cout << result << endl; 	
	}
	

	return 0;
}
