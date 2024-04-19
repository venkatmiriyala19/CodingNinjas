public class Solution {

    public static void deleteAlternateNodes(Node<Integer> head) {
        int count=0;
        Node current=head;
        while(current!=null){
            count++;
            current=current.next;
        }
        current=head;
        if (count%2!=0){
        while(current.next!=null){
            if (current.next.next!=null){
            current.next=current.next.next;
            current=current.next;
            }
            
        }
        }
        else{
            while(current.next.next!=null){
            if (current.next.next!=null){
            current.next=current.next.next;
            current=current.next;
            }
            
        }
        // System.out.print(current.data);
                    current.next=null;

        }
        //Your code goes here
    }
}
