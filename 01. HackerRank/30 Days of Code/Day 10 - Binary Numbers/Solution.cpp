#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    
    int count = 0;
    int max = 0;
    
    while (n > 0)
    {
        
        if (n % 2 == 1)
        {
            count = count + 1;
            
            if (count > max)
            {
                max = count;
            }
            
        }
        
        else
        {
            count  = 0;
        }
        
        n = n / 2;
    }
    
    cout << max << endl;
    
    return 0;
    
}
