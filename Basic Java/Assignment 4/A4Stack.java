public class A4Stack<T> implements Stack<T> {
	private A4Node<T> head;
	
	
	public A4Stack(){
		head = null;
	}
	
	public void push(T value){
		A4Node<T> n = new A4Node<T>(value);
		if(head == null){
			head = n;
		}
		else{
			A4Node<T> cur = head;
			head = n;
			head.next = cur;
		}
	}
	
	public T pop(){
		if (head == null){
			return null;
		}
		else{
			A4Node<T> cur = head;
			if(cur.next == null){
				head = null;
				return cur.getData();
			}
			head = head.next;
			return cur.getData();
			
		}
	}
	 
	
	public boolean isEmpty(){
		return (head == null);
		
	}
	
	public T top(){
		if(this.isEmpty()){
			return null;
		}
		else{
			return head.getData();
		}
	}
	
	public void popAll(){
		head = null;
		
	}
	
}