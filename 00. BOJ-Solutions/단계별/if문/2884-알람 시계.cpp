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
		
		if (M-T >= 0) // M�� 45�к��� Ŀ�� �ڸ��� ������ �߻����� ���� �� 
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
