public interface A3List {

	/* 
	 * Purpose: add s to the front of the list
	 * Parameters: String s - the string to add
	 * Returns: nothing
	 * Precondition: s is not null
	 */
	public void addFront(String s);

	/* 
	 * Purpose: add s to the back of the list
	 * Parameters: String s - the string to add
	 * Returns: nothing
	 * Precondition: s is not null
	 */
	public void addBack(String s);
	
	/* 
	 * Purpose: get the current size of the list
	 * Parameters: none
	 * Returns: int - number of elements in list
	 */
	public int size(); 
	
	/* 
	 * Purpose: determines if the list is empty
	 * Parameters: none
	 * Returns: boolean - true if empty, false otherwise
	 */
	public boolean isEmpty();
	
	/* 
	 * Purpose: removes the element from the front of the list
	 * Parameters: none
	 * Returns: nothing
	 */
	public void removeFront();
	
	/* 
	 * Purpose: removes the element from the back of the list
	 * Parameters: none
	 * Returns: nothing
	 */
	public void removeBack();
	
	/* 
	 * Purpose: rotates the elements in the list right by n spots
	 * Parameters: int n - number of positions to rotate
	 * Returns: nothing
	 * Precondition: n >= 0
	 * Example: Given a list {a, b, c, d, e, f} and n=2, each
	 *          item would be rotated right two positions.
	 *          Elements that 'rotate' off the back appear 
	 *          at the front, resulting in {e, f, a, b, c, d}
	 */
	public void rotate(int n);
	
		
	/* 
	 * Purpose: interleaves this list with another list
	 * Parameters: A3LinkedList other - the list to interleave with
	 * Returns: nothing
	 * Precondition: Both lists are the same size, with size > 1
	 * Example: If listA:  {a1, a2, a3, a4, a5}
	 *          and listB: {b1, b2, b3, b4, b5}
	 *          and the two lists were interleaved, the result would
	 *          be listA:  {a1, b2, a3, b4, a5}
	 *          and listB: {b1, a2, b3, a4, b5}.
	 * NOTE: The video link in the pdf provides a visual example
	 */
	public void interleave(A3LinkedList other);
}