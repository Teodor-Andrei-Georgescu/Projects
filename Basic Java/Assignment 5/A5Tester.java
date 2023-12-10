import java.util.Arrays;

public class A5Tester {
	
	private static int testPassCount = 0;
	private static int testCount = 0;
	private static double THRESHOLD = 0.1; // allowable margin of error for floating point results
	
    public static void main(String[] args) {
		
		// PART I
		// implement and test each of the following methods
		// found in A5Exercises.java, one at a time
		
		testCountMultiples();
		testDoubleAll();
		testGetMinimum();

		// PART II
		// implement and test each of the following methods
		// found in A5Exercises.java, one at a time.
		// Documentation can be found in Stack.java

		testTotalBooks();
		testTotalPages();
		testAveragePages();
		testContainsBook();
		testStackedCorrectly();
		
		System.out.println("Passed " + testPassCount + " / " + testCount + " tests");
	}

	public static void testCountMultiples() {
		System.out.println("\nStarting countMultiples tests");
		
		int[] arr0 = {};
		int[] arr1 = {5};
		int[] arr2 = {2, 8};
		int[] arr3 = {9, 16, 12, 4, 5, 24, 60};
		
		int result = 0;
		int expected = 0;
		
		result = A5Exercises.countMultiples(arr0, 3);
		expected = 0;
		displayResults(result==expected, "countMultiples of 3 in empty array");

		result = A5Exercises.countMultiples(arr1, 3);
		expected = 0;
		displayResults(result==expected, "countMultiples of 3 in arr1");
		
		result = A5Exercises.countMultiples(arr1, 5);
		expected = 1;
		displayResults(result==expected, "countMultiples of 5 in arr1");

		result = A5Exercises.countMultiples(arr2, 3);
		expected = 0;
		displayResults(result==expected, "countMultiples of 3 in arr2");
		
		result = A5Exercises.countMultiples(arr2, 2);
		expected = 2;
		displayResults(result==expected, "countMultiples of 2 in arr2");

		result = A5Exercises.countMultiples(arr2, 4);
		expected = 1;
		displayResults(result==expected, "countMultiples of 4 in arr2");
		
		result = A5Exercises.countMultiples(arr3, 3);
		expected = 4;
		displayResults(result==expected, "countMultiples of 3 in arr3");
		
		result = A5Exercises.countMultiples(arr3, 2);
		expected = 5;
		displayResults(result==expected, "countMultiples of 2 in arr3");

		result = A5Exercises.countMultiples(arr3, 5);
		expected = 2;
		displayResults(result==expected, "countMultiples of 5 in arr3");

		result = A5Exercises.countMultiples(arr3, 60);
		expected = 1;
		displayResults(result==expected, "countMultiples of 60 in arr3");
	}

	public static void testDoubleAll() {
		System.out.println("\nStarting doubleAll tests");
		
		int[] arr0 = {};
		int[] arr1 = {7, 1, 3};
		int[] arr2 = {9, 2, 7, 3, 0, 6};
		
		int[] expected0 = {};
		int[] expected1 = {14, 2, 6};
		int[] expected2 = {28, 4, 12};
		int[] expected3 = {18, 4, 14, 6, 0, 12};
		
		A5Exercises.doubleAll(arr0);
		displayResults(Arrays.equals(arr0, expected0), "double all values in empty array");
		
		A5Exercises.doubleAll(arr1);
		displayResults(Arrays.equals(arr1, expected1), "double all values in arr1");
		
		A5Exercises.doubleAll(arr1);
		displayResults(Arrays.equals(arr1, expected2), "double all values in updated arr1");
		
		A5Exercises.doubleAll(arr2);
		displayResults(Arrays.equals(arr2, expected3), "double all values in arr2");
	}
	
	public static void testGetMinimum() {
		System.out.println("\nStarting getMinimum tests");
		int[] arr0 = {};
		int[] arr1 = {7};
		int[] arr2 = {7, 8};
		int[] arr3 = {8, 7};
		int[] arr4 = {1, 2, 3, 4, 5};
		int[] arr5 = {9, 8, 7, 6, 5};
		int[] arr6 = {8, 7, 1, 3, 6, 2, 4, 9};
		int[] arr7 = {9, 4, 2, 6, 3, 1, 7, 8};
		int[] arr8 = {0, -1, -2, -3, -2, -1, 0};
		
		int result = 0;
		int expected = 0;
		
		result = A5Exercises.getMinimum(arr0);
		expected = -1;
		displayResults(result==expected, "minimum of empty array");
		
		result = A5Exercises.getMinimum(arr1);
		expected = 7;
		displayResults(result==expected, "minimum of arr1");
		
		result = A5Exercises.getMinimum(arr2);
		expected = 7;
		displayResults(result==expected, "minimum of arr2");
		
		result = A5Exercises.getMinimum(arr3);
		expected = 7;
		displayResults(result==expected, "minimum of arr3");
		
		result = A5Exercises.getMinimum(arr4);
		expected = 1;
		displayResults(result==expected, "minimum of arr4");
		
		result = A5Exercises.getMinimum(arr5);
		expected = 5;
		displayResults(result==expected, "minimum of arr5");
		
		result = A5Exercises.getMinimum(arr6);
		expected = 1;
		displayResults(result==expected, "minimum of arr6");
		
		result = A5Exercises.getMinimum(arr7);
		expected = 1;
		displayResults(result==expected, "minimum of arr7");
		
		result = A5Exercises.getMinimum(arr8);
		expected = -3;
		displayResults(result==expected, "minimum of arr8");
	}
	
	public static void testTotalBooks() {
		System.out.println("\nStarting totalBooks tests");
		
		Book b1 = new Book("Gone Girl", "Gillian Flynn", 432);
		Book b2 = new Book("Divergent", "Veronica Roth", 487);
		Book b3 = new Book("Allegiant", "Veronica Roth", 526);
		Book b4 = new Book("Hunger Games", "Suzanne Collins", 374);
		Book b5 = new Book("Mockingjay", "Suzanne Collins", 390);
		Book b6 = new Book("Jade City", "Fonda Lee", 560);
		
		Book[] arr1 = {b1};
		Book[] arr2 = {b1, b2, b3};
		Book[] arr3 = {b1, b2, b3, b4, b5, b6};
		
		A5Stack<Book> s0 = new A5Stack<Book>();
		A5Stack<Book> s1 = new A5Stack<Book>(arr1);
		A5Stack<Book> s2 = new A5Stack<Book>(arr2);
		A5Stack<Book> s3 = new A5Stack<Book>(arr3);
		
		int result = 0;
		int expected = 0;
		
		result = A5Exercises.totalBooks(s0);
		expected = 0;
		displayResults(result==expected, "total books in empty stack");
		
		result = A5Exercises.totalBooks(s1);
		expected = 1;
		displayResults(result==expected, "total books in s1");
		
		result = A5Exercises.totalBooks(s2);
		expected = 3;
		// System.out.println(result);
		displayResults(result==expected, "total books in s2");
		
		result = A5Exercises.totalBooks(s3);
		expected = 6;
		// System.out.println(result);
		displayResults(result==expected, "total books in s3");	
	}
	
	public static void testTotalPages() {
		System.out.println("\nStarting totalPages tests");
		
		Book b1 = new Book("Gone Girl", "Gillian Flynn", 432);
		Book b2 = new Book("Divergent", "Veronica Roth", 487);
		Book b3 = new Book("Allegiant", "Veronica Roth", 526);
		Book b4 = new Book("Hunger Games", "Suzanne Collins", 374);
		Book b5 = new Book("Mockingjay", "Suzanne Collins", 390);
		Book b6 = new Book("Jade City", "Fonda Lee", 560);
		
		Book[] arr1 = {b1};
		Book[] arr2 = {b1, b2, b3};
		Book[] arr3 = {b1, b2, b3, b4, b5, b6};
		
		A5Stack<Book> s0 = new A5Stack<Book>();
		A5Stack<Book> s1 = new A5Stack<Book>(arr1);
		A5Stack<Book> s2 = new A5Stack<Book>(arr2);
		A5Stack<Book> s3 = new A5Stack<Book>(arr3);
		
		int result = 0;
		int expected = 0;
		
		result = A5Exercises.totalPages(s0);
		expected = 0;
		displayResults(result==expected, "total pages in empty stack");
		
		result = A5Exercises.totalPages(s1);
		expected = 432;
		displayResults(result==expected, "total pages in s1");
		
		result = A5Exercises.totalPages(s2);
		expected = 432 + 487 + 526;
		// System.out.println(result);
		displayResults(result==expected, "total pages in s2");
		
		result = A5Exercises.totalPages(s3);
		expected = 432 + 487 + 526 + 374 + 390 + 560;
		// System.out.println(result);
		displayResults(result==expected, "total pages in s3");	
	}
	
	public static void testAveragePages() {
		System.out.println("\nStarting averagePages tests");
		
		Book b1 = new Book("Gone Girl", "Gillian Flynn", 432);
		Book b2 = new Book("Divergent", "Veronica Roth", 487);
		Book b3 = new Book("Allegiant", "Veronica Roth", 526);
		Book b4 = new Book("Hunger Games", "Suzanne Collins", 374);
		Book b5 = new Book("Mockingjay", "Suzanne Collins", 390);
		Book b6 = new Book("Jade City", "Fonda Lee", 560);
		
		Book[] arr1 = {b1};
		Book[] arr2 = {b1, b2, b3};
		Book[] arr3 = {b1, b2, b3, b4, b5, b6};
		
		A5Stack<Book> s0 = new A5Stack<Book>();
		A5Stack<Book> s1 = new A5Stack<Book>(arr1);
		A5Stack<Book> s2 = new A5Stack<Book>(arr2);
		A5Stack<Book> s3 = new A5Stack<Book>(arr3);
		
		double result = 0.0;
		double expected = 0.0;
		
		result = A5Exercises.averagePages(s0);
		expected = 0.0;
		displayResults(Math.abs(result-expected)<THRESHOLD, "average pages in empty stack");
		
		result = A5Exercises.averagePages(s1);
		expected = 432/1.0;
		displayResults(Math.abs(result-expected)<THRESHOLD, "average pages in s1");
		
		result = A5Exercises.averagePages(s2);
		expected = (432 + 487 + 526)/3.0;
		// System.out.println(result);
		displayResults(Math.abs(result-expected)<THRESHOLD, "average pages in s2");
		
		result = A5Exercises.averagePages(s3);
		expected = (432 + 487 + 526 + 374 + 390 + 560)/6.0;
		// System.out.println(result);
		displayResults(Math.abs(result-expected)<THRESHOLD, "average pages in s3");	
	}
	
	public static void testContainsBook() {
		System.out.println("\nStarting containsBook tests");
		
		Book b1 = new Book("Gone Girl", "Gillian Flynn", 432);
		Book b2 = new Book("Divergent", "Veronica Roth", 487);
		Book b3 = new Book("Allegiant", "Veronica Roth", 526);
		Book b4 = new Book("Hunger Games", "Suzanne Collins", 374);
		Book b5 = new Book("Mockingjay", "Suzanne Collins", 390);
		Book b6 = new Book("Jade City", "Fonda Lee", 560);
		
		Book[] arr1 = {b1};
		Book[] arr2 = {b1, b2, b3};
		Book[] arr3 = {b1, b2, b3, b4, b5, b6};
		
		A5Stack<Book> s0 = new A5Stack<Book>();
		A5Stack<Book> s1 = new A5Stack<Book>(arr1);
		A5Stack<Book> s2 = new A5Stack<Book>(arr2);
		A5Stack<Book> s3 = new A5Stack<Book>(arr3);
		String s0Contents = s0.toString();
		String s1Contents = s1.toString();
		String s2Contents = s2.toString();
		String s3Contents = s3.toString();
		
		boolean result = false;
		boolean expected = false;
		
		result = A5Exercises.containsBook(s0, b1);
		expected = false;
		displayResults(result==expected, "empty stack contains b1");
		
		result = A5Exercises.containsBook(s1, b1);
		expected = true;
		displayResults(result==expected, "s1 contains b1");
		displayResults(s1Contents.equals(s1.toString()), "stack unchanged");
		
		result = A5Exercises.containsBook(s1, b2);
		expected = false;
		displayResults(result==expected, "s1 contains b2");
		displayResults(s1Contents.equals(s1.toString()), "stack unchanged");
		
		result = A5Exercises.containsBook(s2, b1);
		expected = true;
		displayResults(result==expected, "s2 contains b1");
		displayResults(s2Contents.equals(s2.toString()), "stack unchanged");
		
		result = A5Exercises.containsBook(s2, b3);
		expected = true;
		displayResults(result==expected, "s2 contains b3");
		displayResults(s2Contents.equals(s2.toString()), "stack unchanged");
		
		result = A5Exercises.containsBook(s2, b4);
		expected = false;
		displayResults(result==expected, "s2 contains b4");
		displayResults(s2Contents.equals(s2.toString()), "stack unchanged");
		
		result = A5Exercises.containsBook(s3, b1);
		expected = true;
		displayResults(result==expected, "s3 contains b1");
		displayResults(s3Contents.equals(s3.toString()), "stack unchanged");
		
		result = A5Exercises.containsBook(s3, b3);
		expected = true;
		displayResults(result==expected, "s3 contains b3");
		displayResults(s3Contents.equals(s3.toString()), "stack unchanged");
		
		result = A5Exercises.containsBook(s3, b6);
		expected = true;
		displayResults(result==expected, "s3 contains b4");
		displayResults(s3Contents.equals(s3.toString()), "stack unchanged");
	}
	
	public static void testStackedCorrectly() {
		System.out.println("\nStarting stackedCorrectly tests");
		
		Book b1 = new Book("Gone Girl", "Gillian Flynn", 432);
		Book b2 = new Book("Divergent", "Veronica Roth", 487);
		Book b3 = new Book("Allegiant", "Veronica Roth", 526);
		Book b4 = new Book("Hunger Games", "Suzanne Collins", 374);
		Book b5 = new Book("Mockingjay", "Suzanne Collins", 390);
		Book b6 = new Book("Jade City", "Fonda Lee", 560);
		
		Book[] arr1 = {b1}; // trivially correct
		Book[] arr2 = {b1, b2}; // stacked correctly
		Book[] arr3 = {b2, b1};
		Book[] arr4 = {b4, b5, b1, b2, b3, b6}; // stacked correctly
		Book[] arr5 = {b5, b4, b1, b2, b3, b6}; // first two out of order
		Book[] arr6 = {b4, b5, b1, b2, b6, b3}; // bottom two out of order
		
		A5Stack<Book> s0 = new A5Stack<Book>();
		A5Stack<Book> s1 = new A5Stack<Book>(arr1);
		A5Stack<Book> s2 = new A5Stack<Book>(arr2);
		A5Stack<Book> s3 = new A5Stack<Book>(arr3);
		A5Stack<Book> s4 = new A5Stack<Book>(arr4);
		A5Stack<Book> s5 = new A5Stack<Book>(arr5);
		A5Stack<Book> s6 = new A5Stack<Book>(arr6);
		String s0Contents = s0.toString();
		String s1Contents = s1.toString();
		String s2Contents = s2.toString();
		String s3Contents = s3.toString();
		String s4Contents = s4.toString();
		String s5Contents = s5.toString();
		String s6Contents = s6.toString();
		
		boolean result = false;
		boolean expected = false;
		
		result = A5Exercises.stackedCorrectly(s0);
		expected = true;
		displayResults(result==expected, "empty stack stacked correctly");
		displayResults(s0Contents.equals(s0.toString()), "stack unchanged");
		
		result = A5Exercises.stackedCorrectly(s1);
		expected = true;
		displayResults(result==expected, "s1 stacked correctly");
		displayResults(s1Contents.equals(s1.toString()), "stack unchanged");
		
		result = A5Exercises.stackedCorrectly(s2);
		expected = true;
		displayResults(result==expected, "s2 stacked correctly");
		displayResults(s2Contents.equals(s2.toString()), "stack unchanged");

		result = A5Exercises.stackedCorrectly(s3);
		expected = false;
		displayResults(result==expected, "s3 stacked correctly");
		displayResults(s3Contents.equals(s3.toString()), "stack unchanged");

		result = A5Exercises.stackedCorrectly(s4);
		expected = true;
		displayResults(result==expected, "s4 stacked correctly");
		displayResults(s4Contents.equals(s4.toString()), "stack unchanged");		
		
		result = A5Exercises.stackedCorrectly(s5);
		expected = false;
		displayResults(result==expected, "s5 stacked correctly");
		displayResults(s5Contents.equals(s5.toString()), "stack unchanged");

		result = A5Exercises.stackedCorrectly(s6);
		expected = false;
		displayResults(result==expected, "s6 stacked correctly");
		displayResults(s6Contents.equals(s6.toString()), "stack unchanged");
	}
	
	public static void displayResults (boolean passed, String testName) {
		testCount++;
		if (passed) {
			System.out.println ("Passed test: " + testName);
			testPassCount++;
		} else {
			System.out.println ("Failed test: " + testName + " at line "
				+ Thread.currentThread().getStackTrace()[2].getLineNumber());
		}
    }
}