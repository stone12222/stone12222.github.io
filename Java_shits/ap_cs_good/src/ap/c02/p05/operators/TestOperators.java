package ap.c02.p05.operators;

public class TestOperators {
	public static void main(String[] args) {
		// Arithmetic operators
		System.out.println(2 / 4);
		System.out.println(2.0 / 4);
		System.out.println(2 / 4.0);

		System.out.println((int) 2.0 / 4);
		System.out.println((double) 2 / 4);
		System.out.println((double) (2 / 4));

		// precedence
		/*-
		 1. casting
		 2. parentheses
		 3. *,/,%
		 4. +,-
		 */
		System.out.println(((double) 3 + 2) / (12 - 2) + 100);

		// Relational operators
		// >,<,==,>=,<=,!=
		// only compare primitive, not reference type
		System.out.println(100 == 100);

		String s1 = new String("abc");
		String s2 = new String("abc");
		System.out.println(s1 == s2);
		System.out.println(s1.equals(s2));

		/*-
		 logical operators
		 !, && ||
		
		 short-circuit evaluation: evaluation stops as soon as the value of
		 the entire expression is known, e.g. for ||, if the first expression
		 is true, then the entire expression is true irrespective of the value
		 of the second expression
		 */

		/*-
		 assignment operators
		 =, +=, -=, *=, /=, %=
		 */

		/*-
		 increment/decrement operators:
		 ++,--
		 */

		/*-
		 operator precedence: page 77
		 */
	}

}


