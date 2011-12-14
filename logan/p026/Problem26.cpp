#include <iostream>
using namespace std;

int cycle( int);

int main(){
    int max = 0;
    int max_cycle = 0;
    int temp_cycle = 0;

    for( int i = 1 ; i < 1000 ; i++){
	cout << i << " cycle: " << cycle(i)<< endl;
	temp_cycle = cycle(i);
	if( temp_cycle > max_cycle){
	    max_cycle = temp_cycle;
	    max = i;
	}

    }

    cout << max_cycle << " " << max << endl;
}

int cycle( int n){

    long nines = 9;
    long temp = (long)n;
    int index = 0;

    while( temp % 2 == 0){
	temp /= 2;
    }

    while( temp % 5 == 0){
	temp /= 5;
    }

    if( temp == 1){
	//index == 0
    }
    else{
	index = 1;

	while( nines % temp != 0){
	    nines = (nines * 10) + 9;
	    index++;
	}
    }

    return index;
}
