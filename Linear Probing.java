import java.util.* ;
import java.io.*; 
import java.util.List;

public class Solution {

    public static int[] linearProbing(List<Integer> keys) {
        int n= keys.size();
        int[] arr=new int[n];
        Arrays.fill(arr,-1);
        for (Integer i:keys){
            int rem=i%n;
            if (arr[rem]==-1){
                arr[rem]=i;
            }
            else{
                while(arr[rem]!=-1 && rem<n){
                    rem++;
                    if(rem==n){
                        rem=0;
                    }
                }
               
                
                arr[rem]=i;
            }
        }
        return arr;
        // Write your code here.
    }

}
