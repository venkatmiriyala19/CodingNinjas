public class Solution {

    static Node insert(int k, int val, Node head) {
        if (k==0){
            Node current=head;
            while(current.next!=head){
                current=current.next;
            }
            Node temp=new Node(val);
            temp.next=head;
            head=temp;
            current.next=head;
            return head;
        }
        Node current=head;
        Node prev=null;
        for (int i=0;i<k;i++){
            prev=current;
            current=current.next;
        }
        Node temp=new Node(val);
        prev.next=temp;
        temp.next=current;
        return head;
        // Write your code here.
        
    }
}
