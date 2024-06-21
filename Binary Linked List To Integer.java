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

public class Solution {
    public static int binaryToInteger(int n, Node head) {
        StringBuilder str=new StringBuilder();
        while(head!=null){
            
             String str1=String.valueOf(head.data);
            // n1+=(n1>>1)*head.data;
            str.append(str1);
            head=head.next;
        }
        String s=str.toString();
        // String str=String.valueOf(n1);
        // System.out.println(str);
        int dec=Integer.parseInt(s,2);
        return dec;
        // Write your code here.
    }
}
