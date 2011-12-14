import java.util.*; //needed for Arrays.sort()

public class Problem52{
    public static void main(String args[]){
	Integer x; //using wrapper to access toString() method
	boolean found_answer_flag = false;

	for( x = 1; !found_answer_flag ; x++){
	    char[][] temp = new char[6][]; //this array will hold the 6 "strings" representing 
					   //1*x, 2*x, ... , 6*x

	    for( Integer i = 0 ; i < 6 ; i++){ //Again, using Integer for the toString() method
		Integer tmp = x * (i + 1); //the next line would have dereference problems without tmp standing in.
		temp[i] = tmp.toString().toCharArray();
		Arrays.sort(temp[i]);
	    } //At this point, char[][] temp is fully initialized and all numbers in each "row" are sorted

	    found_answer_flag = true; //Setting flag to (most likely) be flipped. If it isn't flipped, program stops
	    for( int i = 0 ; i < 6 ; i++){ //Checking if all 6 char[] sequences are the same
		String tmp = String.copyValueOf( temp[0]); //Need to convert back to String for 
							   //String.contentEquals(String)... there isn't a
							   //char[].compare(char[]) method

		if( ! tmp.contentEquals( String.copyValueOf( temp[i]))){ //compare all to the first one
		    found_answer_flag = false;
		}
	    }
	}

	x--; //correct for the extra x++ the loop executed

	System.out.println("The answer is " + x.toString());
    }
}
