#include <iostream>

using namespace std;

float funcion(int a);

int main(){
    cout<<funcion(5)<<endl;
}

float funcion(int a){
    return float(a)/2;
}