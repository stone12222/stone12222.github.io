package ap.c05.p04.math;

public class TestMath {
	public static void main(String[] args) {
		// abs, pow, sqrt, random
		System.out.println(Math.pow(3, 2));
		
		System.out.println(Math.sqrt(16));
		
		// [0, 1)
		System.out.println(Math.random());

		//
		double d=Math.random()*101;
		System.out.println(Math.random()); // [0,1)
		System.out.println(Math.random()*101); // [0,100]
		System.out.println((int)Math.random()*101); // [0,100]
		
		// [20,60]
		System.out.println(Math.floor(Math.random()*(60-20+1)+20));
	}
}


