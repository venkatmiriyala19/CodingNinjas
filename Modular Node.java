import java.util.* ;
import java.io.*; 
/********************************************************

    Following is the class structure of the Node class:
    
    class Node
    {
        public:
            int data;
            Node next;
            Node(int data)
            {
                this.data = data;
                this.next = null;
            }
    };

********************************************************/

class Solution {

  public static Node modularNode(int k,Node head) {
    int count=0;
    Node req=null;
    while(head!=null){
      count++;
      if(count%k==0) req=head;
      head=head.next;
    }
    return req;
    // Write your code here.

  }
}
