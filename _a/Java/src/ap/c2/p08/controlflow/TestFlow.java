package ap.c2.p08.controlflow;

public class TestFlow {
	public static void main(String[] args) {
		
		int i=100;
		if (i>100) {
			System.out.println("i is larger then 100");
		} else if (i==100) {
			System.out.println("i is equeal to 100");
		} else {
			System.out.println("i is less then 100");
		}
		
		int n=5;
		while (n<10) {
			System.out.println(n);
			n++;
		}
	}
}
