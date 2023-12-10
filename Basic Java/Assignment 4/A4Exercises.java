public class A4Exercises {
	
	/*
	 * Purpose: determine if the stack of plates has been
	 *          stacked correctly (ie. there is never a plate
	 *          on top of a smaller plate)
	 * Parameters: Stack<Plate> s - a stack of plates
	 * Returns: boolean - true if the plates are stacked correctly
	 *                    false otherwise
	 * Post-condition: the contents of s are not modified
	 */
	public static boolean stackedCorrectly(Stack<Plate> s) {
		Stack<Plate> temp = new A4Stack<Plate>();
		int smaller = 0;
		boolean truth = true;
		while(!s.isEmpty()){
			Plate ptemp = s.pop();
			int diameter = ptemp.getDiameter();
			
			if (smaller > diameter){
					truth = false;
			}
			else{
				smaller = diameter;
			}
			temp.push(ptemp);
		}
		
		while(!temp.isEmpty()){
			s.push(temp.pop());
		}
		
		return truth; // so it compiles
	}
	
	/*
	 * Purpose: insert p into the correct location in the
	 *          stack such that there are no smaller plates 
	 *          below p and no larger plates above p
	 * Parameters: Stack<Plate> s - a stack of plates
	 *             Plate p - the plate to insert into s
	 * Returns: void - nothing
	 * Pre-condition: plates in s have been stacked correctly
	 */
	public static void insertPlate(Stack<Plate> s, Plate p) {
		Stack<Plate> temp = new A4Stack<Plate>();
		int diameter = 0;
		boolean truth = true;

		while(!s.isEmpty()){
			Plate ptemp = s.pop();
			
			if(p.getDiameter() < ptemp.getDiameter() && truth){
				temp.push(p);
				truth = false;
			}
	
		}
		while(!temp.isEmpty()){
			s.push(temp.pop());
		}
		
		if(s.isEmpty()){
			s.push(p);
		}
		
	}
}