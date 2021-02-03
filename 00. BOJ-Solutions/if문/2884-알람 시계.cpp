#include <iostream>
#include <cstdlib>
using namespace std;

int main(void)
{
	int H = 0;
	int M = 0;
	int T = 45;
	
	cin >> H >> M;
	
	if ((H>=0 and H<=23) and (M>=0 and M<=59))
	{
		
		if (M-T >= 0) // M이 45분보다 커서 자릿수 내림이 발생하지 않을 때 
		{
			cout << H << " " << M-T << endl;
		}
		
		if((M-T < 0) and (H-1>=0))
		{
			cout << H-1 << " " << M-T+60 << endl;
		}
		
		else if((M-T < 0) and (H-1<0))
		{
			cout << H-1+24 << " " << M-T+60 << endl;
		}
		
	}
	
	return 0;
}
