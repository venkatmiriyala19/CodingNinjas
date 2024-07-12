import java.util.* ;
import java.io.*; 
/*********************************************************

    Following is the Binary Tree node structure:

    class Node {
        public int data;
        public Node next;
        public Node prev;

        Node(int data) {
            this.data = data;
            this.next = null;
            this.prev = null;
        }
    }
    
************************************************************/

public class Solution {
    public static Node reverseDLLInGroups(Node head, int k) {
        if (head==null || k<=1) return head;

        Node curr=head;
        Node prev=null;
        Node next=null;
        int cnt=0;

        while(curr!=null && cnt<k){
            next=curr.next;
            curr.next=prev;
            curr.prev=next;
            prev=curr;
            curr=next;
            cnt++;
        }
        if (next!=null){
            head.next=reverseDLLInGroups(next,k);
            head.next.prev=head;
        }
        return prev;
        // Write your code here.
    }
}
