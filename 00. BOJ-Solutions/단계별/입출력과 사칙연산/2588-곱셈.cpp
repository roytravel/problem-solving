#include <iostream>
// ��� ������ ��� + �ڿ��� ���� ���ϱ� 
using namespace std;

int getIntLen(int value)
{
	int count = 0;
	
	do
	{
		value = int(value/10);
		count++;
	}while(value > 0);
	
	return count;
}


int main(void)
{
	// ���ڸ� �ڿ��� 
	int N1, N2 = 0;
	
	// �ڿ��� ����
	int L1, L2 = 0; 
	
	// �߰� ��� 
	int N3, N4, N5 = 0;
		
	cin >> N1;
	cin >> N2;
	
	L1 = getIntLen(N1);
	L2 = getIntLen(N2);
	
	if (L1 == 3 and L2 == 3)
	{
		N3 = N1 * (N2 % 10);
		N4 = N1 * ((N2 / 10) % 10);
		N5 = N1 * ((N2 / 100));
		
		cout << N3 << endl;
		cout << N4 << endl;
		cout << N5 << endl;
		
		cout << N1 * N2 << endl;
	}
	
	return 0;
}
