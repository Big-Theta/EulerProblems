#include <iostream>
using namespace std;

int main(){
    long sum = 0L;
    long temp = 0L;

    for( long i = 0L ; i <= 1000L ; i++){

	temp = 1L;
	for( long j = 0L ; j < i ; j++){
	    temp *= i;
	    temp %= 10000000000L;
	}

	sum += temp;
	sum %= 10000000000L;
    }

    sum--;

    cout << sum << endl;
}
