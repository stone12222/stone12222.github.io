package ap.c2.p04.types;


// promotive(value) vs object

public class Primitive {

	/*
	 * 8 primitives:
	 * byte, short, int, char, long, float, double, boolean
	 */
	
	public static void main(String[] args) {
		boolean b=true;
		byte b1=100; // 8 bits
		byte b2=(byte)128; // overflow
		
		short s=300; // 2 bytes
		System.out.println(Short.MAX_VALUE);
		System.out.println(Math.pow(2, 15)-1);
		
		/*-
		 * 00000000 00000000 00000000 00000000
		 * 00000000 00000000 00000000 10000000 = 128
		 * 
		 * 10000000
		 * 01111111
		 * 10000000 = 128
		 * 
		 * 10000000 for byte = -128
		 */
		
		int i=0;
		System.out.println(Integer.MAX_VALUE);
		
		char c='a'; // char is an integer, but 2 types
		System.out.println(c==97);
		System.out.println(c+97);
		
		long l=1000; // 64 bits
		float f=123.456f; // 32 bits
		System.out.println(Float.MAX_VALUE);
		double d=123.456; // 64 bits
		System.out.println(Double.MAX_VALUE);
		System.out.println(Double.POSITIVE_INFINITY);
		
		// cast for primitive
		byte b3=100;
		int j=b3; // implicit casting
		b3=(byte)j; // explicit casting
		System.out.println(b3);
		
	}
}
