import java.util.* ;
import java.io.*; 
public class Solution {
    public static String doorStatus(int n) {
        StringBuilder sb=new StringBuilder();
        for (int i=1;i<=n;i++){
            if (perfect(i)){
                sb.append('1');
            }
            else{
                sb.append('0');
            }
        }
        String result=sb.toString();
        return result;
        // Write your code here.
    }
    static boolean perfect(int n){
        double squareroot=Math.sqrt(n);
        if (squareroot==Math.floor(squareroot)){
            return true;
        }
        return false;
    }
}
