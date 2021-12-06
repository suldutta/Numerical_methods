#include<iostream>

using namespace std;

void square(float *a, int n){
    for(int i = 0; i<n; i++){
        *a *= *a;
        a++;
    }
}

int main(){
    float a[5] = {10.0, 5.0, 20.0, 34.0, 39.2};
    square(a, 5);
    cout << "The square of the array is : ";
    for(int i = 0; i<5; i++){
        cout << a[i] << ", ";
    }
    cout<<endl;
    return 0;
}
