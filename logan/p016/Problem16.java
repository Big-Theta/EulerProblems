import java.util.*;
import java.lang.*;
import java.math.*;

public class Problem16{
    public static void main(String args[]){
	BigInteger sum = BigInteger.valueOf(0);
	BigInteger temp;
	BigInteger product = new BigInteger("1");

	for( int i = 1 ; i <= 100 ; i++){
	    product = product.multiply( BigInteger.valueOf(i));
	}

	System.out.println(product.toString());

	while( product.compareTo( BigInteger.valueOf(0)) != 0){
	    temp = product.mod( BigInteger.valueOf(10));
	    sum = sum.add(temp);
	    product = product.subtract( temp);
	    product = product.divide( BigInteger.valueOf(10));
	}

	System.out.println(sum.toString());
    }
}
