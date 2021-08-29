package ap.c03.p06.varScope;

//
// 1. instance variable 
// 2. static variable 
// 3. block variable 
// 4. local variable
//
public class Variablescope {
	int i = 0; // instance variable
	static int ii; // static variable

	int i1;

	
//	initial block
	{
//		local vars are vars in non static blocks
		i1 = 1;
		int i2 = 2; // block var
		System.out.println("ABC");
	}

//	static block
	static {
		// i++; //because the instance var is not in this scope
	}

	public Variablescope() {
		i1 = i1 + 1;

		// comment out to see the error
		// i2=i2+1;

		int i3 = 3; // local var
	}

	public void method(int i4) {
		int i5 = 5; // local var

		// i3++;

		for (int i6 = 0; i6 < 6; i6++) { // block var
			System.out.println("i6: " + i6);
		}

		nestedMethod();
	}

	private void nestedMethod() {
		// i5++; //i5 is local to 'method' only
	}
}

class Test {
	public static void main(String[] args) {
		// static var available as long as the Class is in JVM
		System.out.println(Variablescope.ii);
		// instance var available as long as the object is not removed by
		// garbage collection
		// instance var is not in the scope of static

		Variablescope varscope = new Variablescope();
		// local var only live in that method or constructor, not even in nested
		// methods
		// block var only live in the block
	}
}


