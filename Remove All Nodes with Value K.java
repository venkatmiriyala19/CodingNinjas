import java.util.* ;
import java.io.*; 
/****************************************************************
    Following is the Linked List node structure

    class Node {
    public:
        int data;
        Node *next;
        Node(int data) {
            this->data = data;
            this->next = NULL;
        }
    };

*****************************************************************/

public class Solution {
    public static Node removeNodes(Node head, int k) {
        // Write your code here.
        Node dummy=new Node(0);
        dummy.next=head;
        Node prev=dummy;
        Node current=head;
        while(current!=null){
            if (current.data==k){
                prev.next=current.next;
                current=current.next;
                continue;
            }
            prev=current;
            current=current.next;
        }
        return dummy.next;
    }
}
