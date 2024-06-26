import java.io.*;
import java.util.* ;

/*
	Following is the structure of the Singly Linked List.	
	class LinkedListNode<T> 
    {
    	T data;
    	LinkedListNode<T> next;
    	public LinkedListNode(T data) 
        {
        	this.data = data;
    	}
	}

*/
public class Solution 
{
    public static LinkedListNode<Integer> reverseLinkedList(LinkedListNode<Integer> head) 
    {
		
		LinkedListNode current=head;
		LinkedListNode prev=null;
		LinkedListNode next=null;
		while(current!=null){
			next=current.next;
			current.next=prev;
			prev=current;
			current=next;

		}
		return prev;
        // Write your code here!
    }
}
