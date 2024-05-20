public class Solution {

    public static int numsWithProductK(int l, int r, int k) {
        int count=0;
        for(int i=l;i<=r;i++){
            int prod=1;
            int num=i;
            while(num!=0){
                int rem=num%10;
                prod*=rem;
                num/=10;
                if (prod>k){
                    break;
                }
            }
            if (prod==k){
                count++;
            }
        }
        return count;
        // Write your code here
    }
}
