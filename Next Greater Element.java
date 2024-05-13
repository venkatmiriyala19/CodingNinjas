import java.util.* ;
import java.io.*; 

public class Solution {
	
	public static int[] nextGreater(int[] arr, int n) {	
		Stack<Integer> a=new Stack<>();
		int[] ans=new int[n];
		Arrays.fill(ans,-1);
		a.push(arr[n-1]);
		for(int i=n-2;i>=0;i--){
			while(!a.isEmpty() && a.peek()<=arr[i]){
				a.pop();
			}
			if(!a.isEmpty())
				ans[i]=a.peek();
				a.push(arr[i]);
			
		}
		return ans;
		//Write Your code here
		
	}

}
