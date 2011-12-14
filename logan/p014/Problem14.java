public class Problem14{
    public static void main(String args[]){
	int max = 1;
	int maxLength = 0;
	int tempLength = 0;

/*
	for( int i = 1 ; i < 1000000 ; i ++){
	    tempLength = chainLength(i);
	    if( maxLength < tempLength){
		max = i;
		maxLength = tempLength;
	    }

	    if( i % 1000 == 0){
		System.out.println("Progess: " + i);
	    }
	}
	*/

//837799
	chainLength( 837799);
//	System.out.println("Max: " + max + " length: " + maxLength);
    }

    public static int chainLength( int n){
	int count = 1;
	long temp = (long)n;

	while( temp != 1){
	    if( temp % 2 == 0){
		temp /= 2;
	    }
	    else{
		temp = 3 * temp + 1;
	    }

	    count++;
	    System.out.println( temp);
	}

	return count;
    }
}
