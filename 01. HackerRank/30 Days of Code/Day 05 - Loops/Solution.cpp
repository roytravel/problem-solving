#include <bits/stdc++.h>
#include <iostream>
using namespace std;



int main()
{
    int i;
    int n;

    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if (n >= 2 && n <= 20)
        for (i = 1; i <= 10; i++)
            cout << n << " x " << i << " = " << n * i << endl;

    return 0;
}

