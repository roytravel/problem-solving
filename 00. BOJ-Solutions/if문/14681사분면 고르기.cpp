#include <iostream>

using namespace std;

int main(void)
{
	int X = 0;
	int Y = 0;
	
	cin >> X >> Y;
	
	if ((X>=-1000 and X<=1000) and (X!=0) and (Y>=-1000 and Y<=1000) and (Y!=0))
	{
		if (X>0 and Y>0)
			cout << "1" << endl;
		
		if (X<0 and Y>0)
			cout << "2" << endl;
			
		if (X<0 and Y<0)
			cout << "3" << endl;
			
		if (X>0 and Y<0)
			cout << "4" << endl;
	}
}
