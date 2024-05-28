import java.util.*;
public class Solution {

    public static int[] firstAndLastPosition(ArrayList<Integer> arr, int n, int k) {
        int[] arr2=new int[2];
        Arrays.fill(arr2,-1);
        int index=-1;
        for (int i=0;i<n;i++){
            if (arr.get(i)==k){
                if (index==-1){
                arr2[0]=i;
                }
                index=i;
            }
        }
        arr2[1]=index;
        return arr2;
        
        // Write your code here.
    }

};
