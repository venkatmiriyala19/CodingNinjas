import java.util.* ;
import java.io.*; 
/****************************************************************

    Following is the class structure of the Node class:

       	class Node {
    	int data;
    	Node next;

    	Node(int x) {
        	this.data = x;
        	this.next = null;
    	}
};

*****************************************************************/

public class Solution {
    public static Node findPartition(Node head, int X) {
		Node curr=head;
		Node less_head=new Node(0);
		Node great_head=new Node(0);
		Node less=less_head;
		Node great=great_head;
		while(curr!=null){
			if (curr.data<X){
				less.next=curr;
				less=less.next;
			}
			else{
				great.next=curr;
				great=great.next;
			}
			curr=curr.next;
		}
		less.next=great_head.next;
		head=less_head.next;
		great.next=null;
        // Write your code here.
        
		
		return head;
    }
}
