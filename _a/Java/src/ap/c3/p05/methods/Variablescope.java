package ap.c3.p05.methods;

// 1. instance variable: a variable needs object
// 2. static variable
// 3. block variable: variable defined {}
// 4. local variable
public class Variablescope {
	// number is instance variable (object variable)
	int number;
	
	// static variable
	static int age;
	
//	static {
//		int j;
//	}
	
	private void method1(int i) {
		System.out.println(i+100);
	}
	
	public void method2() {
//		System.out.println(this);
	}
	
	// static methods available before new object created
	// because when JVM load class, the static methods available to use
	
	// static methods can only access static member
	static void method3() {
		System.out.println(age);
		
	}
	
	public static void main(String[] args) {
		Variablescope v=new Variablescope();
		Variablescope.method3();
	}
}
