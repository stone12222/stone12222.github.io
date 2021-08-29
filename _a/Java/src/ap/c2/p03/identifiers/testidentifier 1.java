package ap.c2.p03.identifiers;

/*
 * variable name
 * parameters name
 * methods name
 * classes name
 * constants name
 */

// Identifiers are names

public class testidentifier {
	// final means we cannot change the value after init
	// static means we can use the variable directly without creating an object
	final static int CONSTANT=0;
	
	int age = 10;
	
	public void setAge(int age) {
		this.age = age;
	}
	
	public static void main(String[] args) {
		System.out.println(CONSTANT);
		
		testidentifier test=new testidentifier();
		System.out.println(test.age);
	}
}
