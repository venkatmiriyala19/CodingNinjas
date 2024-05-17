import java.util.* ;
import java.io.*; 
/**********************************************************

    Following is the class structure of the Node class:

    class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

***************************************************************/

public class Solution {
	public static Node getListAfterAddingNodes(Node head, int k) {
        if (head==null){
            return null;
        }
        int sum=0;
        int count=0;
        Node current=head;
        Node prev=null;
        while(current!=null){
            count++;
            sum+=current.data;
            if(count==k){
                
                Node temp=new Node(sum);
                
                temp.next=current.next;
                current.next=temp;
                current=current.next;
                count=0;
                sum=0;
            }
            prev=current;
            current=current.next;

        }
        if (count<k && count>0 ){
            Node temp=new Node(sum);
            prev.next=temp;
            temp.next=null;
        }
        // for(int i=0)
        return head;
        // Write your code here.
    }
}
