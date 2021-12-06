#include<iostream>

using namespace std;

float Square(float a){
    return(a*a);
}

int main(){
    float a;
    cout << "enter a  input number : "; 
    cin >> a;
    float b = Square(a);
    cout << "The square of the number is : " << b << endl;
    return 0;
}
