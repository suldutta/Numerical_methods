#include<iostream>
#include "f3.h"

using namespace std;

int main(){
    float a = 10.0;
    float b = 20.0;
    float c = max(a, b);
    cout << "The max of the numbers is : " << c << endl;
    return 0;
}
