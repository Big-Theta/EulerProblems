#include <iostream>
#include <cmath>
using namespace std;

int nth_digit( long, int);
bool works( long);

int main(){
    long tmp = 1020304050607080900L;
    long tmp2 = 0L;
    long upper = sqrt( tmp) + 1000000L;
    long insert[9];
    long temp = 0;

    for( int i = 0 ; i < 9 ; i++){
	insert[i] = (long)pow( 10., ((i) * 2) + 1);
    }

    long i = 123456789L;
    int j = 12345;

    for( j = 0 ; j < 10 ; j++){
	temp += nth_digit( i, (int)(j + 1)) * insert[j];
    }

    for( long i = 0 ; i < 1000000000L ; i++){
	temp = 0L;
	tmp2 = 0L;
	for( j = 0 ; j < 10 ; j++){
	    temp += nth_digit( i, (int)(j + 1)) * insert[j];
	}

	tmp2 = temp + tmp;
	if( works( (long)sqrt(tmp2))){
	    cout << tmp2 << " works" << endl;
	}
	else if( tmp2 == (long)sqrt(tmp2) * (long)sqrt(tmp2)){
	    cout << tmp2 << " almost works" << endl;
	}

	if( i % 10000000 == 0L){
	    cout << " progress: " << i << " " << tmp2 << endl;
	}
    }

/*
    for( long i = sqrt( 100030405060708090L) - 1000000L ; i <= upper ; i++){
	if( works( i)){
	    cout << i << endl;
	    break;
	}

	if( i % 10000000L == 0L){
	    cout << "Progress: " << i << endl;
	}
    }
    */
}

int nth_digit( long x, int n){
    long pow = 1;
    for( int i = 1 ; i < n ; i++){
	pow *= 10L;
    }

    if( n == 0)
	return 0;
    else
	return (int)((x / pow) % 10L);
}

bool works( long x){
//    x = x * x;

    if( nth_digit( x, 1) == 0
     && nth_digit( x, 3) == 9
     && nth_digit( x, 5) == 8
     && nth_digit( x, 7) == 7
     && nth_digit( x, 9) == 6
     && nth_digit( x, 11) == 5
     && nth_digit( x, 13) == 4
     && nth_digit( x, 15) == 3
     && nth_digit( x, 17) == 2
     && nth_digit( x, 19) == 1 ){
	return true;
     }
     else{
	return false;
     }
}
