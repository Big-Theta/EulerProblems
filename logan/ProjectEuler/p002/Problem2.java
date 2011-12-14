public class Problem2{
    public static void main(String args[]){
	int a = 1;
	int b = 2;
	int temp = 0;
	int sum = 2;

	do{
	    temp = a + b;
	    a = b;
	    b = temp;

	    if( b % 2 == 0)
		sum += b;

	}while( b <= 4000000);

	System.out.println(sum);
    }
}
