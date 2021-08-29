package ap.c02.p04.types;

public class Storage_number {
	public static void main(String[] args) {
//		store int
//		01111111111111111111111111111111
		int b=0b001111111111111111111111111111111;
		System.out.println(b);
		int b1=Integer.MAX_VALUE;
		System.out.println(b1);
		
		double s=2147483648.0;
		
		System.out.println((int)s);
		
		
//		when converting point number to binary number
//		will not get accurate result
		double d1=0.7+0.1;
		double d2=0.9-0.1;
		System.out.println(d1);
		System.out.println(d2);
		System.out.println(d1==d2);
		
		System.out.println();
	}
}

//floating point number  32 bits
//double point number  64 bits
//
//integer number 32 bits
//long integer number 64bits