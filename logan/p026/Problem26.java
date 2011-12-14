import java.util.*;
import java.math.*;

public class Problem26{
    public static void main(String args[]){
	int max = 0;
	int max_cycle = 0;
	int temp_cycle = 0;

	for( int i = 7 ; i < 1000 ; i++){
	    temp_cycle = cycle(i);
	    if( temp_cycle > max_cycle){
		max_cycle = temp_cycle;
		max = i;
	    }

	}

	System.out.println(max);
	System.out.println(max_cycle);
    }

    public static int cycle( int n){
	BigInteger nines = BigInteger.valueOf(9);
	BigInteger temp = BigInteger.valueOf(n);
	int index;

	while( temp.mod( BigInteger.valueOf(2) ).compareTo( BigInteger.valueOf(0)) == 0){
	    temp = temp.divide( BigInteger.valueOf(2) );
	}

	while( temp.mod( BigInteger.valueOf(5) ).compareTo( BigInteger.valueOf(0)) == 0){
	    temp = temp.divide( BigInteger.valueOf(5) );
	}

	if( temp.compareTo( BigInteger.valueOf(1)) == 0){
	    index = 0;
	}
	else{
	    index = 1;

	    while( nines.mod(temp).compareTo( BigInteger.valueOf(0)) != 0){
		nines = nines.multiply(BigInteger.valueOf(10)).add( BigInteger.valueOf(9));
		index++;
	    }
	}

	return index;
    }
}
