package ap.c8.p02.writingrecursive;

public class TestRecursion {
	
	static int max=0;
	// recursion 
	static void method1() {
		max++;
		System.out.println("method1 running");
		if (max==5) { //base case
			return;
		}
		// recursive case
		method1();
	}
	
	public static void main(String[] args) {
		method1();
	}
}
