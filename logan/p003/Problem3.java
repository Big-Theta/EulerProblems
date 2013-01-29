import java.util.*;
import java.lang.*;
import java.math.*;

public class Problem3{
    public static void main(String args[]){
	ArrayList<Long> factors = new ArrayList<Long>();
	Long n = new Long("600851475143");
	Long index = new Long(1);

	for( Long i = new Long("3") ; i <= n ; i += 2 ){
	    while( n % i == 0){
		factors.add( i);
		n /= i;

		System.out.println("This is a factor: " + i);
	    }
	}

	Collections.sort( factors);

	for( Long a : factors){
	    System.out.println( a.toString());
	}
    }
}
