#include <iostream>

using namespace std;

int main(void)
{
	int score = 0;
	
	cin >> score;
	
	if (score >= 90 and score <=100)
		cout << "A" << endl;
	
	else if(score >=80 and score <=89)
		cout << "B" << endl;
	
	else if(score >=70 and score <=79)
		cout << "C" << endl;
	
	else if(score >=60 and score <=69)
		cout << "D" << endl;
		
	else
		cout << "F" << endl;
		
	return 0;
}
