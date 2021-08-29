package ap.c08.p02.writingrecursive;

public class FactorialByLoop {

	public static int factorial(int n) {
		int r = 1;
		for (int i = 1; i <= n; i++) {
			r *= i;
		}
		return r;
	}

	public static void main(String[] args) {
		System.out.println(factorial(4));
	}

}


