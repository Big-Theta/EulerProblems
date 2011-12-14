public class Problem7{
    public static void main(String args[]){
	int primes = 0;
	long index = 1;

	do{
	    index++;

	    if( isPrime( index)){
		primes++;
	    }
	}while(primes != 10001);

	System.out.println( index);
    }

    public static boolean isPrime( long n){
	boolean toReturn = true;
	long sqrtOfN = (long)Math.sqrt(n) + 1;

	if( n == 2)
	    return true;

	for( long a = 2 ; a < sqrtOfN && toReturn == true ; a++){
	    if( n % a == 0){
		toReturn = false;
	    }
	}
	return toReturn;
    }
}
