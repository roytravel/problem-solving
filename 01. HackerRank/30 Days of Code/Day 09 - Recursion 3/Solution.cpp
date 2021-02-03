#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// Complete the factorial function below.
int factorial(int n) 
{
    if (n == 0)
        return 1;
    
    return n * factorial(n -1);

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = factorial(n);

    cout << result << "\n";

    return 0;
}

