package ap.c2.p05.operators;

public class TestOperators {
	public static void main(String[] args) {
		// precedence
		/*-
		 1. casting
		 2. parentheses
		 3. *,/,%
		 4. +,-
		 */
		
		// relational operator => boolean
		// >,>=,<,<=,==,!= 
		System.out.println(100>90);
		System.out.println(100!=90);
		System.out.println(100==90);
		
		// logical operator
		// &&, || (short circuit operator)
		/*-
		 truth table

		 for && (and)
		 T	&& T =>	T	
		 T	&& F => F
		 F  && T => F
		 F  && F => F
		 
		 for || (or)
		 T	|| T =>	T	
		 T	|| F => T
		 F  || T => T
		 F  || F => F
		 */
		System.out.println(true && false);
		System.out.println(true || false);
		
		// &&, || (short circuit operator)
		System.out.println(false && (100/0==0));
		System.out.println(true || (100/0==0.1));
		
		// increment, decrease
		int i=100;
		i=i+1; // i++
		i--;
		
		// assignment operators
		// =, +=, -=, *=, /=, %		
		i+=100; // i=i+100;
		i-=100;
		i*=100;
		i/=100;
		i%=100;
		
		//
		System.out.println(8%3);
	}
}


