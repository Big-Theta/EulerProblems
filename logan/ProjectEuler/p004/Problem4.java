import java.util.*;
import java.math.*;
import java.lang.*;

public class Problem4{
    public static void main(String args[]){
	int max = 0;
	int product;
	int[] digits = new int[10];

	for( int i = 0 ; i < 1000 ; i++){
	    for( int j = 0 ; j < 1000 ; j++){
		product = i * j;
		if( isPalindrome( product)){
		    if( product > max)
			max = product;
		}
	    }
	}

	System.out.println(max);
    }

    public static boolean isPalindrome( int n){
	int magnitude = 1;
	int digits = 0;
	int powerOfTen = 1;
	boolean toReturn = true;

	while( magnitude <= n){
	    magnitude *= 10;
	    digits++;
	}

	int[] theDigits = new int[digits];

	for( int i = 0 ; i < digits ; i++){

	    powerOfTen = 1;
	    for( int j = 0 ; j < i ; j++){
		powerOfTen *= 10;
	    }
	    theDigits[i] = (n % (powerOfTen * 10)) / powerOfTen;
	}

	for( int i = 0 ; i < digits ; i++){
//	    System.out.println("n: " + n + " Digit: " + theDigits[i] + " Other end: " + theDigits[ digits - i - 1]);
	    if( theDigits[i] != theDigits[ digits - i - 1])
		toReturn = false;
	}

	return toReturn;
    }
}
