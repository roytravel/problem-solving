#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    
    // Declare second integer, double, and String variables.
    int myInt;
    double myDouble;
    string myString;
    string temp;

    // Read and save an integer, double, and String to your variables.
    getline(cin, temp);
    myInt = stoi(temp);

    getline(cin, temp);
    myDouble = stod(temp);

    getline(cin, myString);
    
    // Print the sum of both integer variables on a new line.
    cout << i + myInt << endl;
    
    // Print the sum of the double variables on a new line.
    cout << fixed << setprecision(1) << d + myDouble << endl;

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout << s << myString << endl;

    return 0;
}