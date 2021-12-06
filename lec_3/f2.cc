#include<iostream>

using namespace std;

float max(float a, float b){
    float c;
    if(a>b)
        c = a;
    else
        c = b;
    return(c);
}

int main(){
    float a = 10.0;
    float b = 20.0;
    float c = max(a, b);
    cout << "The max of the numbers is : " << c << endl;
    return 0;
}
