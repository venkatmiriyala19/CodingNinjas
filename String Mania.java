import java.util.* ;
import java.io.*; 
public class Solution {
	public static int stringMania(int n, int m, String str1, String str2) {
		if (str1.equals(str2)){
			return 0;
		}
		int a=str1.length();
		int b=str2.length();
		if (a<=b){
			for (int i=0;i<a;i++){
				int z=(int)str1.charAt(i);
				int y=(int)str2.charAt(i);
				if (z>y){
					return 1;
				}
				if (z<y){
					return -1;
				}
			}
			return -1;
		}
		else{
			for (int i=0;i<b;i++){
				int z=(int)str2.charAt(i);
				int y=(int)str1.charAt(i);
				if (z>y){
					return -1;
				}
				if (z<y){
					return 1;
				}
			}
			return 1;
		}

		// Write your code here.
	}
}
