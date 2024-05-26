import java.util.*;
public class Solution {
    public static List<Integer> solve(int n, int[] arr, int q, int[][] queries) {
    
        // ArrayList<Integer> list=new ArrayList<>();
        List<Integer> list=new ArrayList<>();
        for (int i=0;i<queries.length;i++){
            if(queries[i][0]==0){
                arr[queries[i][1]]=queries[i][2];
            }
            if(queries[i][0]==1){
                int count=0;
                for(int j=queries[i][1];j<=queries[i][2];j++){
                    if(arr[j]%2==0){
                        count++;
                    }
                }
                list.add(count);
            }
             if(queries[i][0]==2){
                int count=0;
                for(int j=queries[i][1];j<=queries[i][2];j++){
                    if(arr[j]%2!=0){
                        count++;
                    }
                }
                list.add(count);
            }
        }
        return list;
        // Write your code here.
    }

}
