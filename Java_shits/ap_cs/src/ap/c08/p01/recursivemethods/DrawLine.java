package ap.c08.p01.recursivemethods;

public class DrawLine {
	public void drawLine(int n) { // tail recursion method
		if (n == 0)
			System.out.println("end!");
		else {
			for (int i = 1; i <= n; i++)
				System.out.print("*");
			System.out.println();
			drawLine(n - 1);
		}
	}

	public static void main(String[] args) {
		new DrawLine().drawLine(5);
	}
}

// a method that has no pending statements following the recursion call is 'tail
// recursion'


