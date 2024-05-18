import java.util.* ;
import java.io.*; 
/*************************
 * Following is the linked list node class
    class Node {
        
        int data;
        Node next;

        Node(int val) {
            this.data = val;
            next = null;
        }
    }

 ***************/

public class Solution {

    public static Node intersect_ll(Node L1, Node L2) {
        Node current1=L1;
        Node current2=L2;
        Node dummy=new Node(-1);
        Node prev=dummy;
        // Node prev2=null;
        // dummy.next=prev;
        while(current1!=null && current2!=null){
            if(current1.data<current2.data){
                current1=current1.next;
            }
            else if(current2.data<current1.data) {
                current2=current2.next;
            }
            else{
                Node temp=new Node(current2.data);
                prev.next=temp;
                prev=prev.next;
                current1=current1.next;
            current2=current2.next;
            }
            
        }
        return dummy.next;
        
        // Write your Code here
    }   
}
