/****************************************************************

 Following is the class structure of the Node class:

 class Node {
     public int data;
     public Node next;
     public Node prev;

     Node()
     {
         this.data = 0;
         this.next = null;
         this.prev = null;
     }

     Node(int data)
     {
         this.data = data;
         this.next = null;
         this.prev = null;
     }

     Node(int data, Node next)
     {
         this.data = data;
         this.next = next;
         this.prev = next;
     }
 };

 *****************************************************************/

public class Solution
{
    public static Node removeKthNode(Node head, int K)
    {
        Node curr=head;
        int count=0;
        while(curr!=null){
            count++;
            curr=curr.next;
        }
        curr=head;
        Node prev=null;
        if (count==K){
            head=head.next;
            return head;
        }
        while(count!=K){
            prev=curr;
            curr=curr.next;
            count--;
        }
        
        prev.next=curr.next;
        curr.next=null;
        return head;
        // Write your code here.
    }
}
