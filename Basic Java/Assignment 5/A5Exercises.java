public class A5Exercises {

	// PART 1

	/*
	 * Purpose: get a count of the number of elements in the array
	 *          with a value that is a multiple of x
	 * Parameters: int[] arr
	 * Returns: int - the number multiples of x
	 * Pre-condition: x > 0
	 * Post-condition - the array contents are unchanged
	 */
	public static int countMultiples(int[] arr, int x) {
		if (arr.length ==0){
			return 0;
		}
		return countMultiplesHelper(arr, x, arr.length-1);
	}
	private static int countMultiplesHelper(int[] arr, int x, int index){
		if(index == 0){
			if (arr[index] % x == 0){
				return 1;
			}
			else{
				return 0;
			}
		}
		else{
			if(arr[index] % x == 0){
				return 1+ countMultiplesHelper(arr,x,index-1);
			}
			else{
				return 0 + countMultiplesHelper(arr,x,index-1);
			}
		}
	}
		
	/*
	 * Purpose: double all values in the given array
	 * Parameters: int[] array - the array to modify
	 * Returns: void - nothing
	 */
	public static void doubleAll(int[] array) {
		if(array.length == 0){
		}
		else{
		array = doubleAllHelper(array,array.length-1);
		}
	}
	
	private static int[] doubleAllHelper(int[] array, int index){
		if(index == 0){
			array[index] = array[index]*2;
		}
		else{
			array[index] = array[index]*2;
			doubleAllHelper(array,index-1);
		}
		return array;
	}
	
	/*
	 * Purpose: get the minimum value found in the array
	 * Parameters: int[] array - the array to search
	 * Returns: int - minimum value found in the array
	 *                or -1 if the array is empty
	 * Post-condition - the array contents are unchanged
	 */
	public static int getMinimum(int[] array) {
		if(array.length == 0){
			return -1;
		}
		
		return getMinimumHelper(array, array.length-1, array.length-1);
	}
	
	private static int getMinimumHelper(int[] array, int index, int minIndex){
		if(index == -1){
			return array[minIndex];
		}
		else{
			
			if(array[index] < array[minIndex] ){
				return getMinimumHelper(array, index-1, index);
			}
			else{
				return getMinimumHelper(array, index-1, minIndex);
			}
		}
	
	}
	
	



	// PART II

	/*
	 * Purpose: get the total number of books in s
	 * Parameters: Stack<Book> s - the stack of books
	 * Returns: int - the total number of books
	 * Post-condition: s is not modified
	 */
	public static int totalBooks(Stack<Book> s) {
		if(s.isEmpty()){
			return 0;
		}
		Book book = s.pop();
		int count = 1;
		int rest = totalBooks(s);
		
		s.push(book);
	return 1 +rest; // so it compiles
	}
	
	/*
	 * Purpose: get the total number of pages of all 
	 *          books in the stack
	 * Parameters: Stack<Book> s - the stack of books
	 * Returns: int - the total number of pages
	 * Post-condition: s is not modified
	 */
	public static int totalPages(Stack<Book> s) {
		if(s.isEmpty()){
			return 0;
		}
		Book book = s.pop();
		int page = book.getPages();
		int rest= totalPages(s);
		
		s.push(book);
		return page + rest; // so it compiles
	}
	
	/*
	 * Purpose: get the average number of pages of books in s
	 * Parameters: Stack<Book> s - the stack of books
	 * Returns: double - the average number of pages
	 *                   0.0 if there are no books in s
	 * Post-condition: s is not modified
	 */
	public static double averagePages(Stack<Book> s) {
		// You don't need to change this, if you have
		// completed the previous two exercises
		// correctly, it should pass all the tests
		if (s.isEmpty()) {
			return 0.0;
		} else {
			double sum = totalPages(s);
			int count = totalBooks(s);
			return sum/count;
		}
	}

	/*
	 * Purpose: determine whether toFind is contained in s
	 * Parameters: Stack<Book> s - the stack of books
	 *             Book toFind - the book to search for
	 * Returns: boolean - true if s contains toFind, false otherwise
	 * Post-condition: s is not modified
	 */
	public static boolean containsBook(Stack<Book> s, Book toFind) {
		boolean found = false;
		if(s.isEmpty()){
			return found;
		}
		Book book = s.pop();
		if(book == toFind){
			found = true;
		}
		else{
			found = containsBook(s,toFind);
		}
		s.push(book);
		return found; // so it compiles
	}

	/*
	 * Purpose: determine the books in s are stacked correctly
	 *          (ie. there is never a book stacked on top of 
	 *               another book with fewer pages)
	 * Parameters: Stack<Book> s - the stack of books
	 * Returns: boolean - true if books in s are stacked correctly
	 * Post-condition: s is not modified
	 */
	public static boolean stackedCorrectly(Stack<Book> s) {
		boolean truth = true;
		if(s.isEmpty()){
			return truth; 
		}
		Book book = s.pop();
		int topPages = book.getPages();
		
		if(s.top() == null){
			s.push(book);
			return truth;
		}
		else{
			int topStackPages = s.top().getPages();
			if(topPages <= topStackPages){
				truth = stackedCorrectly(s);
			}
			else{
				truth = false;
			}
		}
		s.push(book);
		return truth; // so it compiles
	}
}