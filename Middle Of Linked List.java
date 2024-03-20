public class Solution
{
    public static Node findMiddle(Node head)
    {
        Node slow=head;
        Node fast=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        return slow;

        // Write your code here.
    }
}
