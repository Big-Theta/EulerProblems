import java.math.*;

public class Problem10{
    public static void main(String args[]){
	long sum = 0;

	for( int i = 2 ; i < 2000000 ; i++){
	    if( isPrime( i)){
		sum += i;
	    }
	}

	System.out.println( sum);
    }

    public static boolean isPrime( int n){
	boolean toReturn = true;
	int upperBound = (int)Math.sqrt(n) + 1;

	for( int i = 2 ; i < upperBound ; i++){
	    if( n % i == 0){
		toReturn = false;
		break;
	    }
	}

	if( n == 2){
	    toReturn = true;
	}
	else if( n == 1){
	    toReturn = false;
	}

	return toReturn;
    }
}
