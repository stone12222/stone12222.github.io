package ap.c08.p03.recursive_analysis;

public class Fibonacci {
	static int get(int n) {
		if (n==1 || n==2) {
			return 1;
		}else {
			return get(n-2) + get(n-1);
		}
	}
	public static void main(String[] args) {
		int result=Fibonacci.get(5);
		System.out.println(result);
	}
		
	
	
}
