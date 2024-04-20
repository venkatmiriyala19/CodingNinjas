public class Solution {
	public static Node replaceWithSum(Node head) {
		Node current=head;
		Node prev=null;
		Node prev1=head;
		int sum=0;
		while(current!=null){
			if (current.data!=0){
				sum+=current.data;
			}
			else{
				if(prev!=null){
					prev1.data=sum;
					sum=0;
					prev1.next=current.next;
					prev1=prev1.next;
				}
			}
			prev=current;
			current=current.next;
		}
		if (head.data==0 && head.next!=null){
			return head.next;
		}
		
		return head;
		// Write your code here.
	}
}
