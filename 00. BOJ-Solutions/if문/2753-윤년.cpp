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
	int result = -1; // 여부 확인 
	int year = 0; // 입력 연도 

	cin >> year;
	
	if (year>=1 and year<=4000)
	{
		result = checkLeapYear(year);
		cout << result << endl; 	
	}
	

	return 0;
}
