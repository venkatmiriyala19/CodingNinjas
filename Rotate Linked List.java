/****************************************************************

 Following is the class structure of the Node class:

 class Node {
     public int data;
     public Node next;

     Node()
     {
         this.data = 0;
         this.next = null;
     }

     Node(int data)
     {
         this.data = data;
         this.next = null;
     }

     Node(int data, Node next)
     {
         this.data = data;
         this.next = next;
     }
 };

 *****************************************************************/

public class Solution {
    public static Node rotate(Node head, int k) {
        if (k==0 || head==null || head.next==null){
            return head;
        }
        int count=0;
        Node current=head;
        while(current!=null){
            count++;
            current=current.next;
        }
        if(count==k){
            return head;
        }
        k=k%count;
        Node prev=null;
        current=head;
        for(int i=0;i<count-k-1;i++){
            current=current.next;
        }
        prev=current;
        current=current.next;
        Node temp=current;
        while(current.next!=null){
            current=current.next;
        }
        current.next=head;
        prev.next=null;
        return temp;
        // Write your code here.
    }
}
