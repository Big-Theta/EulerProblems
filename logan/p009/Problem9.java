public class Problem9{
    public static void main(String args[]){
	int k = 0;

	for( int i = 1 ; i <= 1000 ; i++){
	    for( int j = i ; j <= ((1000 - i) / 2) + 1 ; j++){
		k = 1000 - i - j;

		if( ( i * i) + ( j * j ) == (k * k))
		    System.out.println(i + " " + j + " " + k + " " + ( i * j * k));
	    }
	}
    }
}
