import java.util.* ;
import java.io.*; 
public class Solution{
    static int[]dp=new int[100001];
    public static int fibonacciNumber(int n){
        if(dp[n]!=0){
            return dp[n];
        }
        int MOD=1000000007;
        dp[0]=0;
        dp[1]=1;
        for(int i=2;i<=n;i++){
            dp[i]=(dp[i-1]+dp[i-2])%MOD;
        }
        return dp[n];
        // Write your code here.
    }
}
