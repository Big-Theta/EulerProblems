#include <iostream>
using namespace std;

#define A_COUNT 6965

void initialize_abundant( int[]);
bool is_sum(int, int[]);
bool is_abundant(int, int[]); //this is designed to use a binary lookup
bool is_abundant_helper(int);
bool is_sum_of_two_abundant(int, int[]);

int main(){
    int count = 0;
    int a_numbers[ A_COUNT ];
    int index = 0;

    initialize_abundant( a_numbers);

    for( int i = 0 ; i <= 28123 ; i++){
	if( !is_sum(i, a_numbers)){
	    count += i;
	}
    }

    cout << count << endl;
}

void initialize_abundant( int a_numbers[]){
    int index = 0;
    for( int i = 0 ; i < 28124 ; i++){
	if( is_abundant_helper( i)){
	    a_numbers[ index] = i;
	    index++;
	}
    }
}

bool is_sum( int n, int a_numbers[]){
    bool to_return = false;
    for( int i = 0 ; i < A_COUNT ; i++){
	if( is_abundant( (n - a_numbers[i]), a_numbers)){
	    to_return = true;
	    break;
	}
    }

    return to_return;
}

bool is_abundant(int n, int a_numbers[]){ //binary search
    int first = 0, last = A_COUNT;
    bool to_return = false;
    int temp = 0;

    while( last > first){
	temp = first + ((last - first) / 2);
	if( a_numbers[ temp ] == n){
	    to_return = true;
	    last = 0; //basically break
	}
	else if( a_numbers[ temp ] < n){
	    if(first == temp){
		first++;
	    }
	    else{
		first = temp;
	    }
	}
	else if( a_numbers[ temp ] > n){
	    if( last == temp){
		last--;
	    }
	    else{
		last = temp;
	    }
	}
    }

    return to_return;
}

bool is_abundant_helper(int n){

    bool to_return = false;
    int count = 0;

    for( int i = 1 ; i < n ; i++){ //i == 1 to avoid floating point exception
	if( n % i == 0){
	    count += i;
	}
    }

    if( count > n)
	to_return = true;

    return to_return;
}

bool is_sum_of_two_abundant( int n, int a_numbers[]){
    for( int i = 0 ; i < A_COUNT ; i++){
	
    }
}
