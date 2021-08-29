package ap.c08.p04.recursive_helper;

/*
i:
5

o:
15 (because 1+2+3+4+5)
 */
public class FindSumCheckInput {
	private static int sum(int n) {
		if (n == 1)
			return 1;
		else
			return n + sum(n - 1);
	}

	public static int getSum(int n) throws IllegalArgumentException {
		if (n > 0)
			return sum(n);
		else
			throw new IllegalArgumentException("n must be positive");
	}

	public static void main(String[] args) {
		System.out.println(getSum(5));
		System.out.println(getSum(-1));
	}

}

