import java.util.* ;
import java.io.*; 
/****************************************************************

    Following is the class structure of the DLLNode class:

    class DLLNode {
    int data;
	DLLNode next, prev;

	DLLNode(int data) {
		this.data = data;
		this.next = null;
		this.prev = null;
	}
}

*****************************************************************/

public class Solution 
{
	public static DLLNode rotateDLL(DLLNode head, int k)
    {
		DLLNode curr=head;
		int count=0;
		while(curr!=null){
			curr=curr.next;
			count++;
		}
		k=k%count;
		DLLNode rotate=head;
		curr=head;
		while(k!=0){
			rotate=rotate.next;
			k--;
		}
		DLLNode last=rotate.prev;
		last.next=null;
		last=rotate;
		while(last.next!=null){
			last=last.next;
		}
		last.next=head;
		return rotate;
		 //Write your code here
	}
}

