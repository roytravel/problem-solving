#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// Complete the solve function below.
void solve(double meal_cost, int tip_percent, int tax_percent)
{
	
	double one_hundread = 100.00;
	double totalCost = 0;

	totalCost = round(meal_cost + (meal_cost * tip_percent / one_hundread) + (meal_cost * tax_percent / one_hundread));
	
	cout << totalCost << endl;
}

int main()
{
	double meal_cost;
	cin >> meal_cost;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');

	int tip_percent;
	cin >> tip_percent;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');

	int tax_percent;
	cin >> tax_percent;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');

	solve(meal_cost, tip_percent, tax_percent);

	return 0;
}

