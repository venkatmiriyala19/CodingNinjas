import java.util.* ;
import java.io.*; 

public class Solution {
    static int[] detectOdd(int n, int nums[]) {
        int arr[]=new int[2];
        HashMap<Integer,Integer> freq=new HashMap<>();
        for(int num:nums){
            freq.put(num,freq.getOrDefault(num,0)+1);
        }
        int k=0;
        for (int i=0;i<nums.length;i++){
            if(freq.get(nums[i])%2!=0){
                arr[k]=nums[i];
                k++;
            }
        }
        Arrays.sort(arr);
        return arr;
        // Write your code here.

    }
}
