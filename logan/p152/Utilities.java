import java.util.*;
import java.math.*;

public class Utilities{ //Note... this assumes that only one Utilities object is ever made... this limitation does not currently impede its purpose. 
    static BigInteger comDenom;
    static BigInteger knapsackTarget;
    static int hits = 0;
    static int showProgress = 0;
    static int progressTicker = 0;

    public Utilities( int min, int max){
	set_comDenom( min, max);
	set_knapsackTarget( min, max);
    }

    private static void set_comDenom(int min, int max){

	int temp;
	List<Integer> factors = new ArrayList<Integer>();
	List<Integer> allFactors = new ArrayList<Integer>();

	for( int i = min ; i <= max ; i++){
	    temp = i * i;
	    factors.clear(); //clear the list for each loop

	    for( int j = 2 ; j <= i ; j++){
		while( temp % j == 0){
		    factors.add(j);
		    temp /= j;
		}
	    }

	    Collections.sort(factors);
	    Collections.sort(allFactors);

	    int trackBall; //counts recurrence of elements
	    int allTrackBall;
	    for( int indexA = min ; indexA <= max ; indexA++){ //lists only contain prime elements, but they might contain that largest element. This checks how many times the factor indexA appears on both lists
		trackBall = 0;
		allTrackBall = 0;

		for( int indexB = 0 ; indexB < factors.size() ; indexB++){ //find how many times the factor indexA appears in this list
		    if( factors.get(indexB) == indexA){
			trackBall++;
		    }
		}

		for( int indexC = 0 ; indexC < allFactors.size() ; indexC++){ //find how many times the factor indexA appears in this list
		    if( allFactors.get(indexC) == indexA)
			allTrackBall++;
		}

		if( trackBall > allTrackBall){ //How many more copies of this factor do we need to introduce to allFactors?
		    for( int indexD = allTrackBall ; indexD < trackBall ; indexD++){
			allFactors.add( indexA);
		    }
		}
	    }
	}

	Collections.sort(allFactors);

	BigInteger tempry = BigInteger.valueOf(1);

	for( int i = 0 ; i < allFactors.size() ; i++){
	    tempry = tempry.multiply( BigInteger.valueOf( allFactors.get(i)));
	}

	comDenom = tempry;
    }

    public static BigInteger return_comDenom(){
	return comDenom;
    }

    public static BigInteger[] numerators( int min, int max){
	BigInteger[] toReturn = new BigInteger[ max - min + 1]; //usually will be 79, but if max and min are "1" then we need to add 1.
	BigInteger temp = return_comDenom();

	for( int i = 0 ; i < max - min + 1 ; i++){ //consistency in expressions...
	    toReturn[ i] = temp.divide( BigInteger.valueOf((i + min) * (i + min)) );
//	    System.out.println("This: " + i + ": " + toReturn[i].toString());
	}

	return toReturn;
    }

    private static void set_knapsackTarget( int min, int max){
	BigInteger temp = return_comDenom();

	temp = temp.divide( BigInteger.valueOf( 2));

	knapsackTarget = temp;
    }

    public static BigInteger return_knapsackTarget(){
	return knapsackTarget;
    }

    public static int return_hits(){
	return hits;
    }

    public void knapsackRecursion( BigInteger[] numerators, int currentPossition, BigInteger currentSum, int min, int max){ //initial call uses currentPossition == 0
    //how far along... the current possition
    //either include this one, or don't. We need to do both, actually. 
    //We don't add something if adding it exceeds our target. 

	if( currentPossition < max - min + 1){ //each recursion doubles the nodes introduced. This will be slow. 
	    BigInteger ifAdded = currentSum.add( numerators[ currentPossition]);
	    BigInteger ifNotAdded = currentSum;

	    //ADD THIS ONE:
	    if( ifAdded.compareTo( return_knapsackTarget()) > 0 ){ //sum too large
		//do nothing...don't continue recursion
	    }
	    else if( currentSum.compareTo( return_knapsackTarget()) == 0){
		hits++; //increment hits... is this correct? 
		//don't continue recursion
	    }
	    else{ //recursive call
		showProgress();
		knapsackRecursion( numerators, currentPossition + 1, ifAdded, min, max);
	    }

	    //DON'T ADD THIS ONE: Don't need checks because they were in higher level. 
	    showProgress();
	    knapsackRecursion( numerators, currentPossition + 1, ifNotAdded, min, max);
	}
    }

    public void showProgress(){
	showProgress++;

	if(showProgress == 100000000){
	    showProgress = 0;
	    progressTicker++;
	    System.out.println("Working... ticker = " + progressTicker);
	}
    }
}
