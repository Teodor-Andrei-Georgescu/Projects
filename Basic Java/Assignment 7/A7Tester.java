/*
* A7Tester.java
* A test program for Assignment 7.
*/

import java.util.Random;

public class A7Tester {
	private static int testPassCount = 0;
	private static int testCount = 0;
	public static boolean testHeapSolution = true;

	public static void main (String[] args) {
		if (args.length != 0 && args[0].equals("linked")) {
			testHeapSolution=false;
		}

		System.out.println("Testing " + (testHeapSolution ? "Heap" : "Linked" ) + " implementation.");
		
		testSize();
		testInsertionAndRemoval();
		testExceptions();
		testGeneric();
		testDuplicates();
		testMixed();
		stressTest();

		System.out.println("Testing Application using Priority Queue.");
		testAttendee();
		testConcertLine();

		System.out.println("PASSED " + testPassCount + "/" + testCount + " tests");
	}

	public static PriorityQueue createNewPriorityQueue()  {
		if (testHeapSolution) {
			return new HeapPriorityQueue();
		} else {
			return new LinkedPriorityQueue();
		}
	}

	public static PriorityQueue createNewPriorityQueue(int size)  {
		if (testHeapSolution) {
			return new HeapPriorityQueue(size);
		}
		else {
			return new LinkedPriorityQueue();
		}
	}

	public static void testSize() {
		System.out.println("\nBasic testing of size, isEmpty");
		PriorityQueue pq = createNewPriorityQueue();
		
		displayResults (pq.size() == 0, "size on empty PQ");
		displayResults (pq.isEmpty(), "isEmpty on empty PQ");

		pq.insert(10);
		displayResults (pq.size() == 1, "size on 1 element PQ");
		displayResults (!pq.isEmpty(), "isEmpty on 1 element PQ");

		pq.insert(9);
		displayResults (pq.size() == 2, "size on 2 element PQ");

		pq.insert(7);
		displayResults (pq.size() == 3, "size on 3 element PQ");
	}

	public static void testInsertionAndRemoval() {
		System.out.println("\nBasic testing of removeMin");
		PriorityQueue pq = createNewPriorityQueue();
		
		pq.insert(8);
		pq.insert(9);
		pq.insert(10);

		int result;
		result = ((Integer)pq.removeMin()).intValue();
		// System.out.println("res: " + result + ":" + pq);
		displayResults(result == 8, "remove on multiple element PQ");
		displayResults(pq.size() == 2, "remove + size on multiple element PQ");

		result = ((Integer)pq.removeMin()).intValue();
		// System.out.println("res: " + result + ":" + pq);
		displayResults(result == 9, "remove on multiple element PQ");
		displayResults(pq.size() == 1, "remove + size on multiple element PQ");

		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 10, "remove + size on 1 element PQ");
		displayResults(pq.isEmpty(), "remove + isEmpty on 1 element PQ");

		pq = createNewPriorityQueue();
		pq.insert(3);
		pq.insert(2);
		pq.insert(1);

		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 1, "insert + remove on multiple element PQ");
		displayResults(pq.size() == 2, "insert + remove + size on multiple element PQ");

		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 2, "insert + remove on multiple element PQ");
		displayResults(pq.size() == 1, "insert + remove + size on multiple element PQ");

		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 3, "insert + remove on 1 element PQ");
		displayResults(pq.isEmpty(), "insert + remove + size on 1 element PQ");
	}

	public static void testExceptions() {
		System.out.println("\nTesting of exceptions");
		PriorityQueue pq = createNewPriorityQueue(2);

		try {
			pq.removeMin();
			displayResults(false, "exception should have been thrown");
		} catch (HeapFullException e) {
			displayResults(false, "different exception should have been thrown");
		} catch (HeapEmptyException e) {
			displayResults(true, "HeapEmptyException should be thrown");
		}
		
		pq.insert(10);
		pq.insert(9);
		try {
			pq.insert(8);
			if(testHeapSolution) {
				displayResults(false, "exception should have been thrown in heap solution");
			} else {
				displayResults(true, "exception should not have been thrown in linked version");
			} 
		} catch (HeapEmptyException e) {
			displayResults(false, "different exception should have been thrown");
		} catch (HeapFullException e) {
			displayResults(true, "HeapFullException should be thrown");
		}
	}

	public static void testGeneric() {
		System.out.println("\nTesting of removeMin with Strings");
		PriorityQueue pq = createNewPriorityQueue();
		String result;

		pq.insert("abc");
		pq.insert("def");
		pq.insert("ghi");

		result = ((String)pq.removeMin());
		displayResults(result.equals("abc"), "insert/remove Strings");
		displayResults(pq.size() == 2, "insert/remove Strings");

		result = ((String)pq.removeMin());
		displayResults(result.equals("def"), "insert/remove Strings");
		displayResults(pq.size() == 1, "insert/remove Strings");

		result = ((String)pq.removeMin());
		displayResults(result.equals("ghi"), "insert/remove Strings");
		displayResults(pq.isEmpty(), "insert/remove Strings");

		pq = createNewPriorityQueue();
		pq.insert("ghi");
		pq.insert("def");
		pq.insert("abc");

		result = ((String)pq.removeMin());
		displayResults(result.equals("abc"), "insert/remove Strings");
		displayResults(pq.size() == 2, "insert/remove + size Strings");

		result = ((String)pq.removeMin());
		displayResults(result.equals("def"), "insert/remove Strings");
		displayResults(pq.size() == 1, "insert/remove + size Strings");

		result = ((String)pq.removeMin());
		displayResults(result.equals("ghi"), "insert/remove Strings");
		displayResults(pq.isEmpty(), "insert/remove + isEmpty Strings");
	}

	public static void testDuplicates() {
		System.out.println("\nTesting duplicates.");
		PriorityQueue pq = createNewPriorityQueue();
		int result;

		pq.insert(4);
		pq.insert(1);
		pq.insert(1);
		pq.insert(5);
		pq.insert(0);
		// System.out.println("q after insert 4 1 1 5 0:" + q);
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 0, "add duplicates + remove single");

		pq.insert(4);
		pq.insert(1);
		pq.insert(4);
		pq.insert(4);

		pq.insert(0);
		pq.insert(5);
		pq.insert(0);
		pq.insert(5);

		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 0, "add duplicates + remove duplicates");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 0, "add duplicates + remove duplicates");

		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 1, "add duplicates + remove duplicates");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 1, "add duplicates + remove duplicates");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 1, "add duplicates + remove duplicates");

		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 4, "add duplicates + remove duplicates");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 4, "add duplicates + remove duplicates");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 4, "add duplicates + remove duplicates");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 4, "add duplicates + remove duplicates");

		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 5, "add duplicates + remove duplicates");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 5, "add duplicates + remove duplicates");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 5, "add duplicates + remove duplicates");

		displayResults(pq.isEmpty(), "insert/remove + isEmpty");

	}

	public static void testMixed() {
		System.out.println("\nTesting insert mixed with removeMin.");
		PriorityQueue pq = createNewPriorityQueue();
		int result;
		
		pq.insert(2);
		pq.insert(0);
		pq.insert(5);
		pq.insert(7);

		result = ((Integer)pq.removeMin()).intValue();
		displayResults( result == 0, "inserts + remove");

		pq.insert(4);
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 2, "inserts + remove + insert + remove");

		pq.insert(11);
		pq.insert(2);
		pq.insert(3);
		pq.insert(1);
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 1, "inserts + remove");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 2, "inserts + remove");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 3, "inserts + remove");
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 4, "inserts + remove");

		pq.insert(1);
		result = ((Integer)pq.removeMin()).intValue();
		displayResults(result == 1, "inserts + remove");
		displayResults(pq.size() == 3, "inserts + remove + size");
	}

	public static boolean testRandomArray (int count)
	{
		/* These tests are effectively sorting the random values
			- for the heap, this is O (n log n)
			- for the linked list, this is O (n^2)
		*/
		PriorityQueue q = createNewPriorityQueue(count);
		System.out.println("Testing size: " + count);
		Random r = new Random();
		for ( int i = 0; i < count; i++ ) {
			int val = r.nextInt(1000000);
			q.insert (val);
		}

		int oldVal = 0; //smallest possible value val could be
		int i = 0;
		while (!q.isEmpty()) {
			int val = (int)((Integer)q.removeMin()).intValue(); // or a bug
			if ( val < oldVal ) {
				return false;
			}
			oldVal = val;
			i++;
		}
		return true;

	}

	public static void stressTest() {		
		System.out.println("\nStress Tests.");
		displayResults(testRandomArray(100), "inserts + removes");
		displayResults(testRandomArray(10000), "inserts + removes");
		displayResults(testRandomArray(100000), "inserts + removes");

		//This takes too long using the linked list.
		if (testHeapSolution) {
			displayResults(testRandomArray(1000000), "inserts + removes");
		}
		
	}

	public static void testAttendee() {
		System.out.println("\nTesting Attendee creation, compareTo and equals.");
		Ticket t1a = new Ticket("Taylor Swift", 1, 203);
		Ticket t1b = new Ticket("Taylor Swift", 2, 101);
		Ticket t1c = new Ticket("Taylor Swift", 2, 403);
		Ticket t1d = new Ticket("Taylor Swift", 3, 57);
		Ticket t1e = new Ticket("Taylor Swift", 1, 569);
		
		Attendee a1 = new Attendee("Ali", t1a, new Time(6,30));
		Attendee a2 = new Attendee("Sam", t1b, new Time(6,30));
		Attendee a3 = new Attendee("Lee", t1c, new Time(5,15));
		Attendee a4 = new Attendee("Ola", t1d, new Time(4,10));
		Attendee a5 = new Attendee("Mia", t1e, new Time(6,30));
		Attendee a1Later = new Attendee("Ali", t1a, new Time(8,45));
		Attendee a2Fake = new Attendee("Thief", t1b, new Time(7,10));
		Attendee a3WrongTicket = new Attendee("Lee", t1d, new Time(5,15));
		
		displayResults(a1.compareTo(a2) < 0, "testing attendee compareTo (ticketType)");
		displayResults(a2.compareTo(a1) > 0, "testing attendee compareTo (ticketType)");
		displayResults(a1.compareTo(a3) < 0, "testing attendee compareTo (ticketType)");
		displayResults(a2.compareTo(a3) > 0, "testing attendee compareTo (ticketType and arrivalTime tiebreaker)");
		displayResults(a3.compareTo(a2) < 0, "testing attendee compareTo (ticketType and arrivalTime tiebreaker)");
		displayResults(a4.compareTo(a3) > 0, "testing attendee compareTo (ticketType)");
		displayResults(a1.compareTo(a5) == 0, "testing attendee compareTo (ticketType and arrivalTime tiebreaker)");
		displayResults(a5.compareTo(a1) == 0, "testing attendee compareTo (ticketType and arrivalTime tiebreaker)");
		// Missing some compareTo tests. Add them!
		
		displayResults(a1.equals(a1Later), "same attendee and ticket, re-entering venue");
		displayResults(!a2.equals(a2Fake), "thief using counterfeit ticket");
		displayResults(!a3.equals(a3WrongTicket), "Lee brought the wrong ticket");
	}

	public static void testConcertLine() {
		System.out.println("\nTesting adding/removing attendees from the line at a concert");
		Ticket t1a = new Ticket("Taylor Swift", 1, 203);
		Ticket t1b = new Ticket("Taylor Swift", 2, 101);
		Ticket t1c = new Ticket("Taylor Swift", 2, 403);
		Ticket t1d = new Ticket("Taylor Swift", 3, 57);
		Ticket t1e = new Ticket("Taylor Swift", 1, 569);
		Ticket t1f = new Ticket("Taylor Swift", 2, 101);
		
		Attendee a1 = new Attendee("Ali", t1a, new Time(6,30));
		Attendee a2 = new Attendee("Sam", t1b, new Time(6,30));
		Attendee a3 = new Attendee("Lee", t1c, new Time(5,15));
		Attendee a4 = new Attendee("Ola", t1d, new Time(4,10));
		Attendee a5 = new Attendee("Mia", t1e, new Time(3,55));
		Attendee a6 = new Attendee("Pat", t1f, new Time(7,50));
		
		Attendee nextA = null;

		ConcertLine c1 = new ConcertLine();
		displayResults(c1.numAttendeesWaiting() == 0, "testing ConcertLine constructor + numAttendeesWaiting");

		c1.addAttendee(a2);
		c1.addAttendee(a3);
		c1.addAttendee(a4);

		displayResults(c1.numAttendeesWaiting() == 3, "testing ConcertLine addAttendee + numAttendeesWaiting");
		nextA = c1.nextAttendee();
		// System.out.println(nextA);
		displayResults(a3.equals(nextA), "testing ConcertLine nextAttendee");
		displayResults(c1.numAttendeesWaiting() == 2, "testing ConcertLine nextAttendee + numAttendeesWaiting");

		c1.addAttendee(a1);
		c1.addAttendee(a5);
		c1.addAttendee(a6);
		displayResults(c1.numAttendeesWaiting() == 5, "testing ConcertLine addAttendee + numAttendeesWaiting");

		nextA = c1.nextAttendee();
		// System.out.println(nextA);
		displayResults(a5.equals(nextA), "testing ConcertLine nextAttendee");
		nextA = c1.nextAttendee();
		// System.out.println(nextA);
		displayResults(a1.equals(nextA), "testing ConcertLine nextAttendee");
		displayResults(c1.numAttendeesWaiting() == 3, "testing ConcertLine nextAttendee + numAttendeesWaiting");

		nextA = c1.nextAttendee();
		// System.out.println(nextA);
		displayResults(a2.equals(nextA), "testing ConcertLine nextAttendee");
		nextA = c1.nextAttendee();
		// System.out.println(nextA);
		displayResults(a6.equals(nextA), "testing ConcertLine nextAttendee");
		nextA = c1.nextAttendee();
		// System.out.println(nextA);
		displayResults(a4.equals(nextA), "testing ConcertLine nextAttendee");
		displayResults(c1.numAttendeesWaiting() == 0, "testing ConcertLine nextAttendee + numAttendeesWaiting");

		nextA = c1.nextAttendee();
		displayResults(nextA == null, "testing ConcertLine nextAttendee - no more in line");

		ConcertLine smallVenue = new ConcertLine(2);
		smallVenue.addAttendee(a1);
		smallVenue.addAttendee(a2);

		try {
			smallVenue.addAttendee(a3);
			displayResults(true, "testing ConcertLine addAttendee to full line - should get here without exception");
		} catch (HeapFullException e) {
			displayResults(false, "testing ConcertLine addAttendee to full line - should not get here");
		}
	}

	public static void displayResults (boolean passed, String testName) {
		testCount++;
		if (passed) {
			System.out.println ("Passed test " +testCount+": " + testName);
			testPassCount++;
		} else {
			System.out.println ("Failed test: " + testName + " at line "
								+ Thread.currentThread().getStackTrace()[2].getLineNumber());
		}
	}
}
