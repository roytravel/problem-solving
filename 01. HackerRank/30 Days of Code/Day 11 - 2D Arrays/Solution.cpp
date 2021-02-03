#include <bits/stdc++.h>
#include <iostream>

using namespace std;


int main()
{
    vector<vector<int>> arr(6);
    int sum = 0;
    int max = -7 * 9;
    
    for (int i = 0; i < 6; i++) 
    {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) 
	{
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    
    
    for (int i = 0; i < 6; i++)
    {
    	for (int j = 0; j < 6; j++)
    	{
    		if ((i < 4) && (j < 4))
    		{
    			sum = sum + arr[i][j] + arr[i][j+1] + arr[i][j+2];
			sum = sum + arr[i+1][j+1];
			sum = sum + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
				
			if (sum > max)
			{
				max = sum;
			}
			
		}
			
		sum = 0;
	}
    }
	
    cout << max << endl;
    
    return 0;
}

