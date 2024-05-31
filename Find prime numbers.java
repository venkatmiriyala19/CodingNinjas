import java.util.*;
public class Solution {

	public static ArrayList<Integer> primeNumbersTillN(int N) 
	{ 
	// 	ArrayList<Integer> list=new ArrayList<>();
	// 	for(int i=2;i<=N;i++){
	// 		if(isPrime(i)){
	// 			list.add(i);
	// 		}
	// 	}
	// 	return list;
	//  	// Write your code here
	// }
	// public static boolean isPrime(int n){
	// 	for(int i=2;i<=Math.sqrt(n);i++){
	// 		if(n%i==0) return false;
	// 	}
	// 	return true;
	boolean[] isPrime=new boolean[N+1];
	Arrays.fill(isPrime,true);
	isPrime[0]=false;
	isPrime[1]=false;
	for(int p=2;p*p<=N;p++){
		if (isPrime[p]){
			for(int i=p*p;i<=N;i+=p){
				isPrime[i]=false;
			}
		}
	}
	ArrayList<Integer> list=new ArrayList<>();
	for(int i=2;i<=N;i++){
		if(isPrime[i]){
			list.add(i);
		}
	}
	return list;
	}
}
