import java.util.* ;
import java.io.*; 
public class Solution {
    public static boolean amicablePair(int x, int y){
        int a=0,b=0;
        for (int i=1;i<x;i++){
            if (x%i==0) a+=i;
        }
        for (int j=1;j<y;j++){
            if(y%j==0) b+=j;
        }
        // System.out.print(a+" "+b);
        return a==y && b==x;
        // Write your code here.
    }
}
