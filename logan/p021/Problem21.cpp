#include <iostream>
using namespace std;

int d(int);
bool has_amicable_pair(int);

int main(){
    int count = 0;

    for( int i = 1 ; i < 10000 ; i++){
	if( has_amicable_pair( i)){
	    count += i;
	}
    }

    cout << "result is " << count << endl;

    return 0;
}

int d(int n){

    int to_return = 0;

    for( int i = 1 ; i < n ; i++){
	if( n % i == 0)
	    to_return += i;
    }

    return to_return;
}

bool has_amicable_pair(int a){
    bool to_return = false;
    if( d(a) == a){
	to_return = false;
    }
    else if( d( d(a) ) == a){
	to_return = true;
    }

    return to_return;
}
