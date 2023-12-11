/*
* HeapPriorityQueue.java
*
* An implementation of a minimum PriorityQueue using a heap.
* based on the implementation in "Data Structures and Algorithms
* in Java", by Goodrich and Tamassia
*
* This implementation will throw a Runtime, HeapEmptyException
*	if the heap is empty and removeLow is called.
*
* This implementation will throw a Runtime, HeapFullException
*	if the heap is full and insert is called.
*
*/
@SuppressWarnings({"rawtypes", "unchecked"})
public class HeapPriorityQueue implements PriorityQueue {

	protected final static int DEFAULT_SIZE = 10000;
	
	protected Comparable[] storage;
	protected int currentSize;

	/*
	 * Constructor that initializes the array to hold DEFAULT_SIZE elements
	 */
	public HeapPriorityQueue() {
		// TODO: implement this
		
		// if using a 1-based implementation, remember to allocate an 
		// extra space in the array since index 0 is not used. 
		this.storage = new Comparable[DEFAULT_SIZE];
		this.currentSize=0;
	}
	
	/*
	 * Constructor that initializes the array to hold size elements
	 */
	public HeapPriorityQueue(int size) {
		// TODO: implement this
		
		// if using a 1-based implementation, remember to allocate an 
		// extra space in the array since index 0 is not used.
		this.storage = new Comparable[size+1];
		this.currentSize =0;
	}

	public void insert (Comparable element) throws HeapFullException {
		// TODO: implement this
		
		// When inserting the first element, choose whether to use 
		// a 0-based on 1-based implementation. Whatever you choose,
		// make sure your implementation for the rest of the program
		// is consistent with this choice.
		if(isFull()){
		 throw new HeapFullException();
		}
		storage[currentSize] = element;
		bubbleUp(currentSize);
		currentSize++;
    }
	
	public void bubbleUp(int index) {
		// TODO: implement this
		if(storage[(int)index/2] == null){
			return;
		}
		else if(storage[index].compareTo(storage[(int)index/2]) < 0){
			Comparable temp = storage[index];
			storage[index] = storage[(int)index/2];
			storage[(int)index/2] = temp;
		}
		
		bubbleUp((int)index/2);
	}
			
	public Comparable removeMin() throws HeapEmptyException {
		// TODO: implement this
		if(isEmpty()){
			throw new HeapEmptyException();
		}
		Comparable first = storage[0];
		Comparable last = storage[currentSize];
		storage[0] = last;
		storage[currentSize]=null;
		currentSize--;
		bubbleDown(0);
		return first; // so it compiles
	}
	
	private void bubbleDown(int index) {
		// TODO: implement this
		if (index > currentSize){
			return;
		}
		else if(2*index +1 > currentSize && 2*index+2 > currentSize){
			return;
		}
		else if(2*index +1 <= currentSize && 2*index+2 > currentSize){
			if(storage[index].compareTo(storage[2*index+1])<0){
				Comparable temp = storage[index];
				storage[index] = storage[2*index+1];
				storage[2*index+1] = temp;
				return;
			}
		}
		else if(2*index +1 <= currentSize && 2*index+2 <= currentSize){
			Comparable left = storage[2*index +1];
			Comparable right = storage[2*index+2];
			Comparable min = 0;
			int minI =0;
			if(left != null && right != null){
				if(right.compareTo(left) < 0){
					min = right;
					minI = 2*index+2;
				}else{
					min = left;
					minI = 2*index+1;
				}
				if(min.compareTo(storage[index])<0){
					Comparable temp = storage[index];
					storage[index] = min;
					storage[minI] = temp;
					bubbleDown(minI);
				}
			}
			
			
		}
	}

	public boolean isEmpty(){
		// TODO: implement this
		
		return currentSize==0; // so it compiles
	}
	
	public boolean isFull() {
		// TODO: implement this
		
		return currentSize == DEFAULT_SIZE-1; // so it compiles
	}
	
	public int size () {
		// TODO: implement this
		
		return currentSize; // so it compiles
	}

	public String toString() {
		String s = "";
		String sep = "";
		// This implementation of toString assumes you 
		// are using a 1-based approach. Update the initial
		// and final value for i if using a 0-based
		for(int i=1; i<=currentSize; i++) {
			s += sep + storage[i];
			sep = " ";
		}
		return s;
	}
}
