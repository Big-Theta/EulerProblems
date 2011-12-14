import java.util.*;
import java.math.*;
import java.lang.*;

public class Driver{
    public static void main(String args[]){
	int min, max;
	min = 2;
	max = 20;

	Utilities fiddler = new Utilities( min, max);
	BigInteger[] numerators = new BigInteger[max - min + 1];

	System.arraycopy( fiddler.numerators(min, max), 0 , numerators , 0 , max - min + 1);

	System.out.println( fiddler.return_comDenom().toString());

/*	for( BigInteger a : numerators){
	    System.out.println("The numerators is: " + a);
	}*/

//	fiddler.knapsackRecursion( numerators, 0, BigInteger.valueOf( 0), min, max);

//	System.out.println("Hits: " + fiddler.return_hits());
    }
}
