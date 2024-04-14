public class Solution {
    public static int findIntersection(Node firstHead, Node secondHead) {
        if (firstHead==null || secondHead==null){
            return 0;
        }
        while(secondHead!=null){
            Node temp=firstHead;
            while(temp!=null){
                if (temp==secondHead){
                    return secondHead.data;
                }
                temp=temp.next;
            }
            secondHead=secondHead.next;
        }
        //Write your code here
        return -1;
    }
}
