public class Problem1{
    public static void main(String args[]){

	int toReturn = 0;

	for( int i = 0 ; i < 1000 ; i++){
	    if( i % 3 == 0 || i % 5 == 0){
		toReturn += i;
	    }
	}

	System.out.println( toReturn );
    }
}
