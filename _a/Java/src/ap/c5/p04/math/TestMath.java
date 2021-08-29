package ap.c5.p04.math;

public class TestMath {
	public static void main(String[] args) {
		// abs, pow, sqrt, random
		System.out.println(Math.pow(3, 2));
		System.out.println(Math.sqrt(16));
		
		// [0, 1)
		System.out.println(Math.random());

		// [0,1)*101 = [0,101)
		double d=Math.random()*101;
		System.out.println(d);
		System.out.println(Math.floor(d)); // [0,100]
		System.out.println(Math.ceil(d)); 
		
		// [20,60]
		d=Math.random(); // [0,1)
		d=d*(61-20); // [0,41)
		d=d+20; // [20,61)
		int result=(int)d; //[20,60]
		
		// [min,max]
		int min=20;
		int max=60;
		result=(int)(Math.random()*(max+1-min)+min);
		
		System.out.println((int)(Math.random()*(61-20)+20));
	}
}



