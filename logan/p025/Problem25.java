import java.math.*;

public class Problem25{
    public static void main(String args[]){
	BigInteger n = BigInteger.valueOf(2);
	BigInteger a = BigInteger.valueOf(1);
	BigInteger b = BigInteger.valueOf(1);
	BigInteger temp = b;
	BigInteger cap = BigInteger.valueOf(10).pow(999);

	while( b.compareTo( cap) == -1){
	    temp = b.add(a);
	    a = b;
	    b = temp;
	    n = n.add(BigInteger.valueOf(1));
	}

	System.out.println(b.toString() + " ---- " + n.toString());
    }
}
