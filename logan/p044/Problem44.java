import java.util.*;

public class Problem44{
    public static void main(String args[]){
	ArrayList<Integer> pNumbers = new ArrayList<Integer>();
	int count = 10000;
	int d = 10000000;
	int temp = 0;

	for( int i = 1 ; i <= count ; i++){
	    pNumbers.add( (i * ((3 * i) - 1)) / 2);
	}

	for( int i = 1 ; i < count ; i++){
	    for( int j = 1 ; j < count ; j++){
		if( isPentagonal( pNumbers.get(i) + pNumbers.get(j), pNumbers, count ) 
		    && isPentagonal( pNumbers.get(i) - pNumbers.get(j) , pNumbers, count)){
			temp = 
			    pNumbers.get(i) > pNumbers.get(j) 
			    ? pNumbers.get(i) - pNumbers.get(j) 
			    : pNumbers.get(j) - pNumbers.get(i);

		    d = temp < d ? temp : d;
		}
	    }
	}

	System.out.println(d);
    }

    static boolean isPentagonal( int n, ArrayList<Integer> pNumbers, int count){
	int first = 0, last = count - 1;
	boolean toReturn = false;
	int temp = 0;
	int tempGet = 0;

	while( last > first){
	    temp = first + ((last - first) / 2);
	    tempGet = pNumbers.get(temp);
	    
	    if( tempGet == n){
		toReturn = true;
		last = 0; //basically break
	    }
	    else if( tempGet < n){
		if(first == temp){
		    first++;
		}
		else{
		    first = temp;
		}
	    }
	    else if( tempGet > n){
		if( last == temp){
		    last--;
		}
		else{
		    last = temp;
		}
	    }
	}

	return toReturn;
    }
}
