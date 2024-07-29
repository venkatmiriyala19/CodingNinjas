import java.util.* ;
import java.io.*; 
public class Solution {

    public static int maximumWeightRow(int n, int m, int[][] mat) {
        int summer=0;
        for (int i=0;i<n;i++){
            int temp=0;
            for(int j=0;j<m;j++){
                temp+=mat[i][j];
            }
            if (temp>=summer){
                summer=temp;
            }
        }
        return summer;
        // Write your code here.
    }
}
