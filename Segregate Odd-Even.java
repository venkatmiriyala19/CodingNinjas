/*************************************************************

	Following is the class structure of the Node class:

    class Node {
		public int data;
		public Node next;

		Node(int data) {
			this.data = data;
			this.next = null;
	  	}
    }

*************************************************************/

public class Solution {
	public static Node segregateOddEven(Node head) {
		Node dummy=new Node(-1);
		Node dummy2=new Node(-1);
		dummy.next=head;
		Node curr=head;
		Node odd=dummy;
		Node even=dummy2;
		while(curr!=null){
			if(curr.data%2!=0){
				odd.next=curr;
				odd=odd.next;
			}
			else{
				even.next=curr;
				even=even.next;
			}
			curr=curr.next;
		}
		odd.next=dummy2.next;
		even.next=null;
		return dummy.next;
		// Write your code here.
	}
}
