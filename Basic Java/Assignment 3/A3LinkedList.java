// Name: Teodor Andrei Georgescu
// Student number: v00979120

public class A3LinkedList implements A3List {
	private A3Node head;
	private A3Node tail;
	private int length;
	
	public A3LinkedList() {
		head = null;
		tail = null;
		length = 0;
	}
	
	public void addFront(String s) {
		A3Node n = new A3Node(s);
		if (isEmpty()){
			
			head = n;
		}
		else if(size() ==1) {
		n.next = head;
		tail = head;
		head.prev = n;
		head = n;
		}
		
		else{
			n.next = head;
			head.prev =n;
			head = n;
		}
		this.length++;
		
	}

	public void addBack(String s) {
		A3Node n = new A3Node(s);
		if(isEmpty() ){
			tail = n;
			head = n;
		}
		else if (size() == 1){
			head = tail;
			tail = n;
			head.next = n;
			n.prev = head; 
		}
		else{
			tail.next = n;
			n.prev = tail;
			tail= n;
		
		}
		this.length++;
	}
	
	public int size() {
		return length;
	}
	
	public boolean isEmpty() {
		return length==0;
	}
	
	public void removeFront() {
		if(isEmpty()){
			head = null; 
		}
		
		else if(size() == 1){
			head = null;
			this.length--;
		}
		
		else{
			head = head.next;
			this.length--;
		}
	}
	
	public void removeBack() {
		if (isEmpty()){
			tail = null;
		}
		else if(size() == 1){
			head = null;
			this.length--;
		}
		else{
			tail.next = tail.prev;
			tail = tail.prev;
			tail.next = null;
			this.length--;
		
		}
		
	}
	
	
	public void rotate(int n) {
		
		if(isEmpty()){}
		else if(size() ==1){}
		
		else{
		A3Node last = tail;
		String lastnode = last.getData();
		
		for(int i= 0; i<n; i++){
			this.addFront(lastnode);
			this.removeBack();
			last = tail;
			lastnode = last.getData();
		}
		}
	}
	
	public void interleave(A3LinkedList other) {
		A3Node thisCurrent = this.head;
        A3Node otherCurrent = other.head;
        
        int count = 1;
        while(count <= this.length){
            A3Node otherNext = otherCurrent.next;
         
            otherCurrent.next = thisCurrent.next;
            
            thisCurrent.next = otherNext;
            
            thisCurrent = thisCurrent.next;
			
            otherCurrent = otherCurrent.next;
			
            count += 1;
        }
	}
	
	/*
	 * Purpose: return a string representation of the list 
	 *          when traversed from front to back
	 * Parameters: none
	 * Returns: nothing
	 */
	public String frontToBack() {
		String result = "{";
		A3Node cur = head;
		while (cur != null) {
			result += cur.getData();
			cur = cur.next;
		}
		result += "}";
		return result;
	}
	
	/*
	 * Purpose: return a string representation of the list 
	 *          when traversed from back to front
	 * Parameters: none
	 * Returns: nothing
	 */
	public String backToFront() {
		String result = "{";
		A3Node cur = tail;
		while (cur != null) {
			result += cur.getData();
			cur = cur.prev;
		}
		result += "}";
		return result;
	}
}
	