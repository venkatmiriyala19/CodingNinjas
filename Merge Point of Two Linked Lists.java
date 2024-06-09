/*
    Time Complexity :- O(N)
    Space Complexity :- O(1)
    
    Where N is the maximum length of linked list.
*/

public class Solution {

	private static int length(LinkedListNode<Integer> head) {
	    int length = 0;
	    while (head != null) {
	        head = head.next;
	        length++;
	    }
	    return length;
	}

	public static int findIntersection(LinkedListNode<Integer> firstHead, LinkedListNode<Integer> secondHead) {
		
		 // get the length of both list
		int firstListLength = length(firstHead), secondListLength = length(secondHead);
		 
	    // move headA and headB to the same start point
	    while (firstListLength > secondListLength) {
	    	firstHead = firstHead.next;
	        firstListLength--;
	    }
	    
	    while (firstListLength < secondListLength) {
	    	secondHead = secondHead.next;
	    	secondListLength--;
	    }
	    
	    // find the intersection until end
	    while (firstHead != secondHead) {
	    	firstHead = firstHead.next;
	    	secondHead = secondHead.next;
	    }
	    
	    if(firstHead == null)
	    	return -1;
	    
	    return firstHead.data;
	}
}
