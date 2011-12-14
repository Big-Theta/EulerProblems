import java.math.*;

public class Problem12{
    public static void main(String args[]){
	int triangleNumber = 0;
	int i = 0;

	do{
	    triangleNumber += i; //traingleNumber += ++i; ??
	    i++;

	    if( i % 1000 == 0){
		System.out.println( i);
	    }
	}while( numDivisors( triangleNumber) <= 500);

	System.out.println( numDivisors(triangleNumber) + " the number: " + triangleNumber);
    }

    public static int numDivisors(int n){
	int toReturn = 0;
	int top = (((int)Math.sqrt(n) * (int)Math.sqrt(n)) == n) ? (int)Math.sqrt(n) - 1 : (int)Math.sqrt(n);
	for( int i = 1 ; i < top ; i++){
	    if( n % i == 0){
		toReturn++;
	    }
	}

	toReturn *= 2;

	if( (int)Math.sqrt(n)  == Math.sqrt(n)){
	    toReturn++;
	}

	return toReturn;
    }
}
