#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int nth_digit( long, int);
void set_digit( long&, int, int); //doesn't strictly swap... the smaller digit is placed correctly
void increment( long&);
bool is_permutation( long);

int main(){
    long a = 123456789L;

    for( int i = 1 ; i < 5 ; i++){
	increment( a);

	cout << "i " << setw(3) << i << " : " << a << endl;
    }

    cout << a << endl;

//    for( int i = 0 ; i < 1/*000000*/ ; i++){
/*	for( int j = 0 ; j < 9 ; j++){ //if error, switch 9 for 8
	    if( nth_digit( a, j) > nth_digit( a, j + 1)){
		swap_digits( a, j, j + 1);
		break;
	    }
	}
	*/
//    }

    return 0;
}

int nth_digit(long a, int n){
    int to_return = (int)(a / (long)pow(10.0, (double)(9 - n ))) % 10;
    return to_return;
}

void set_digit( long& a, int n, int x){
    a = a - (nth_digit(a, n) * (long)pow(10, 9 - n));
    a += (long)x * (long)pow(10, 9 - n);
}

void increment( long& a){ //assume p < q
    int tmp = 0;
    int tmp2 = 0;
    for( int i = 9 ; i >= 0; i--){
	if( nth_digit( a, i) > nth_digit( a, i - 1)){
	    tmp = nth_digit( a, i - 1);
	    cout << " here " << a <<  " tmp " << tmp << endl;
	    set_digit( a, i - 1, nth_digit( a, 9));

	    cout << "there " << a << endl;


	    for( int j = i ; j <= 9 ; j++){
		cout << " 1j " << j << " tmp " << tmp << " nth " << nth_digit(a, j) << " a " << a << endl;
//		if( tmp < nth_digit( a, j)){
		    cout << " 2j " << j << " tmp " << tmp << " nth " << nth_digit(a, j) << " a " << a << endl;
		    tmp2 = nth_digit( a, j);
		    set_digit( a, j, tmp);
		    cout << " 3j " << j << " tmp " << tmp << " nth " << nth_digit(a, j) <<  " a " << a << endl;
		    tmp = tmp2;
//		}
	    }
	    cout << "There " << a << endl;

	    break;
	}
    }
}

bool is_permutation( long a){
    int product = 1;
}
