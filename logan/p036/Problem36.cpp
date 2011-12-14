#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Number{
    public:
	Number(int);
	bool both_palindrome();
    private:
	int number_10;
	char number_2[21];
	int number_2_digits;
	int number_10_digits;
	void convert_to_base_2();
	void set_number_10_digits();
	bool number_10_is_palindrome();
	bool number_2_is_palindrome();
	int nth_digit( int, int);
};

int main(){
    Number a(1);
    long count = 0L;
    for( long i = 0 ; i < 1000000 ; i++){
	a = Number((int)i);

	if( a.both_palindrome()){
	    count += i;
	}
    }

    cout << count << endl;
}

Number::Number(int n)
       :number_10 (n), number_2_digits (0){
    convert_to_base_2();
    set_number_10_digits();
}

bool Number::both_palindrome(){
    bool to_return = false;

    if( number_10_is_palindrome() && number_2_is_palindrome()){
	to_return = true;
    }

    return to_return;
}

void Number::convert_to_base_2(){
    int temp = number_10;
    int two_pow = 524288;
    number_2_digits = 0;

    char test = 'a';

    for( int i = 0 ; i < 20 ; i++){ //Note: this creates a "backwards" base2 number.
	if( temp >= two_pow){
	    temp -= two_pow;
	    number_2[i] = '1';

	    if( number_2_digits == 0){
		number_2_digits = 20 - i;
	    }
	}
	else{
	    number_2[i] = '0';
	}
	test++;

	two_pow /= 2;
    }

    number_2[20] = '\0';
}

void Number::set_number_10_digits(){
    int tens = 10;

    for( int i = 0 ; i < 7 ; i++){
	if( number_10 < tens){
	    number_10_digits = ++i;
	    break;
	}

	tens *= 10;
    }
}

bool Number::number_10_is_palindrome(){
    int outer = number_10_digits, inner = 1;
    bool to_return = true;

    for( inner = 1 ; outer > 0 ; inner++, outer--){
	if( nth_digit( number_10, inner) != nth_digit( number_10, outer)){
	    to_return = false;
	    break;
	}
    }

    return to_return;
}

bool Number::number_2_is_palindrome(){
    int outer = 20 - number_2_digits, inner = 19;
    bool to_return = true;

    for( inner = 19; outer < 19 ; inner--, outer++){
	if( number_2[outer] != number_2[inner]){
	    to_return = false;
	    break;
	}
    }

    return to_return;
}

int Number::nth_digit(int x, int n){
    return (int)( x / (int)pow(10.0, (double)(n - 1))) % 10;
}
