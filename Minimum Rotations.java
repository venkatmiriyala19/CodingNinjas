import java.util.* ;
import java.io.*; 
public class Solution {

	public static int minimumRotations(int n, String s) {
		for (int i=0;i<n-1;i++){
			if(s.charAt(i)!=s.charAt(i+1)){
				return n;
			}
		}
		return 1;
		// Write your code here.
	}

}
