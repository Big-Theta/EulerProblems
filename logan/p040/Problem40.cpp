#include <iostream>
#include <cmath>
using namespace std;

int nth_digit(int);

int main(){
    for(int i = 0 ; i < 21 ; i++){
	nth_digit(i);
    }

    return 0;
}

int nth_digit(int n){
    bool found = false;
    int count = 0, temp = 0, digits = 0, nth_digit;

    int i = 0;
    cout << "pre: count: " << count << " digits: " << digits << " n: " << n << " i: " << i << endl;
    for( ; !found ; i++){
	digits = 1;

	while( (int)pow(10., (double)digits) <= i) digits++; //counts the digits

	if(n >= digits){
	    n -= digits;
	}
	else{
	    temp = i;
	    cout << "internal, n: " << n << " i: " << i << " digits: " << digits << endl;
	    for(int j = 0 ; j < n ; j++){
		i /= 10;
	    }

	    nth_digit = i % 10;
	    //
	    found = true;
	}

    }
	cout << "pst: count: " << count << " digits: " << digits << " n: " << n << " i: " << i << " nth_digit: " << nth_digit << endl << endl;
}
