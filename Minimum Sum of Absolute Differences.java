import java.util.* ;
import java.io.*; 
public class Solution {
    public static int minimumSum(int[] arr1, int[] arr2, int n) {
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int abs=0;
        for(int i=0;i<n;i++){
            abs+=(Math.abs(arr1[i]-arr2[i]));
        }
        return abs;
        // Write your code here.
    }
}
