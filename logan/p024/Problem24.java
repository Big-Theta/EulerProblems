import java.util.*;

public class Problem24{
    public static void main(String args[]){
	int index = 1;
	long i;
	int target = 1000000;
	target++;

	for( i = 123456789L ; index < target ; i++){
	    if( isPermutation( i)){
		index++;
	    }

	    if( i % 10000000 == 0){
		System.out.println(i + " : " + index);
	    }
	}

	System.out.println(i - 1);
    }

    static boolean isPermutation( long n){
	Long temp = n < 1023456789L ? n * 10L : n;
	boolean toReturn = false;
	char[] a = temp.toString().toCharArray();
	Arrays.sort(a);
	String tmp = new String( a);

	if( tmp.contentEquals("0123456789")){
	    toReturn = true;
	}

	return toReturn;
    }
}
