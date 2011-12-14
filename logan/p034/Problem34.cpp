#include <iostream>
#include <cmath>
using namespace std;

int nth_digit( long, int);
int factorial( int);
int count_digits( long);
int sum_of_digits( long);

int main(){
    long sum = 0;

    cout << "sum " << sum_of_digits( 40585L) << endl;
/*
    for( long i = 3L ; 1 ; i++){
	if( i == sum_of_digits( i)){
	    sum += i;
	    cout << sum << " " << i << endl;
	}
    }
    */

    return 0;
}

int nth_digit( long x, int n){
    int to_return = (int)(x / (long)pow(10.0, (double)( n - 1 ))) % 10;
    return to_return;
}

int factorial( int n){
    int to_return = 1;

    if( n == 0){
	to_return = 1;
    }
    else{
	for( int i = 1 ; i <= n ; i++)
	    to_return *= i;
    }

    return to_return;
}

int count_digits( long x){
    int digits = 0;

    for( int i = 1 ; i < 10 ; i++){
	if( nth_digit( x, i) != 0){
	    digits = i;
	}
    }

    return digits;
}

int sum_of_digits( long x){
    int sum = 0;
    int bound = count_digits( x);
    for( int i = 1 ; i <= bound ; i++){
	sum += factorial( nth_digit( x, i));
    }

    return sum;
}
