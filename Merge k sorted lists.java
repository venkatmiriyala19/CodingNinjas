/****************************************************
	Following is the Node class for the Singly Linked List

		class LinkedListNode<Integer> {
			int data;
			LinkedListNode<Integer> next;

			public LinkedListNode(int data) {
				this.data = data;
			}
		}

****************************************************/
import java.util.*;
public class Solution {
    public static LinkedListNode<Integer> mergeKLists(LinkedListNode<Integer>[] listArray) {
		ArrayList<Integer> list=new ArrayList<>();
		for (int i=0;i<listArray.length;i++){
			LinkedListNode<Integer> current=listArray[i];
			while(current!=null){
				list.add(current.data);
				current=current.next;
			}
		}
		LinkedListNode<Integer> dummy=new LinkedListNode<>(-1);
		LinkedListNode<Integer> prev=dummy;
		Collections.sort(list);
		for(Integer ele:list){
			LinkedListNode<Integer> temp=new LinkedListNode<>(ele);
			prev.next=temp;
			prev=prev.next;
		}
		return dummy.next;
        // Write your code here.
    }
}
