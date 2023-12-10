public class A2Exercises {

	/*
	 * Purpose: get the number of students in the given course  	
	 *          with a grade above the given grade threshold
	 * Parameters: UvicCourse course
	 *             int gradeThreshold 
	 * Returns: int - the number of enrolled students with 	
	 *                a grade above gradeThreshold
	 */
	public static int countAbove(UvicCourse course, int gradeThreshold) {
		int count = 0;
		
		Student[] classlist = course.getClassList();
		for(int i =0; i < classlist.length; i++){
			if(classlist[i].getGrade() > gradeThreshold){
				count++;
			}
		}
		return count; // so it compiles
	}
	
	/*
	 * Purpose: get the name of the class with the highest average
	 * Parameters: UvicCourse[] courses - the array of courses
	 * Returns: String - the name of the course with the highest average
	 * Precondition: the array has at least one course in it
	 * NOTE: if there are two are more courses with the same class average 
	 *       which is the highest value of all courses in the array,
	 *       the name of course that comes first in the array is returned
	 */
	public static String highestAverage(UvicCourse[] courses) {
		String courseName = courses[0].getName();
		double highestAverage = 0;
		for(int i = 0; i < courses.length; i++){
			if(courses[i].averageGrade() > highestAverage){
				highestAverage = courses[i].averageGrade();
				courseName = courses[i].getName();
			}
		}
		return courseName; // so it compiles
	}
	
	/*
	 * Purpose: get the average grade of the student with given sid
	 *          across all courses the student is enrolled in
	 * Parameters: UvicCourse[] courses - an array of courses
	 *             String sid - the sid of the student for which 
	 *                          to calculate the average grade for
	 * Returns: double - the average grade of the student with given sid
	 *                   -1 if the student is not in any of the courses	 
	 *
	 * Note: the student is not necessarily enrolled in the courses
	 *       found in the given array
	 */
	public static double studentAverage(UvicCourse[] courses, String sid) {
		double average = 0.0;
		int numCourses = 0;
		String sSid = "";
		Student[] classList = {};
		for (int i = 0; i < courses.length; i++){
			classList = courses[i].getClassList();
			for(int n = 0; n < classList.length; n++){
				sSid = classList[n].getSid();
				if(sSid.equals(sid)){
					average += courses[i].getGrade(sid);
					numCourses++;
				}
			}			
		}
		average = average / numCourses;
		return average; // so it compiles
	}
	
}