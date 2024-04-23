public class Solution {

    public static void merge(Node head1, Node head2) {
        
        Node first = head1, second = head2;
        Node f_next = null, s_next = null;

        // Solving for each node in Linkedlist.
        while (first != null)
        {
            // Storing the next pointers.
            f_next = first.next;
            s_next = second.next;

            // Inserting the node of the second LinkedList in the first LinkedList.
            second.next = f_next;
            first.next = second;

            // Updating the current pointers for the next iteration.
            first = f_next;
            second = s_next;
        }
    }   
}
