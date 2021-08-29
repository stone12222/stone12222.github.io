package ap.c2.p04.types;

public class StorageNumber {
	public static void main(String[] args) {
		
		// how to storage a positive number
		/*-
		 * dec		binary
		 * 0		0
		 * 1		1
		 * 2		10
		 * 3		11
		 * 4		100
		 * 5		101
		 * 6		110
		 * 7		111
		 * 8		1000
		 * 9		1001
		 * 10		1010
		 * 11		1011
		 * 12		1100
		 * 13		1101
		 * 14		1110
		 * 15		1111
		 * 16		10000
		 * 17		10001
		 * 18		10010
		 * 19		10011
		 */
		
		//
		byte b=4;
		short b1=4; // 2^2=4
		
		// convert binary to decimal
		short b2=0b100; // binary literal
		System.out.println(b2);
		System.out.println(Integer.toBinaryString(b2));
		
		// how to storage negative number?
		b=-4;
		// 2's complement
		/*
		 * 1. invert
		 * 2. +1
		 */
		/*-
		 * 4 for byte 00000100
		 *-4 for byte 11111011 // invert
		 * 					 1 // +1
		 * 			  11111100 //-4
		 */
		// how to read a negative number
		/*
		 * -4		11111100
		 * 			00000011 // invert
		 * 			00000100 // +1 => 4
		 * 			
		 * 			11111100 => 4
		 */
		/*
		 * excise:
		 * 10110100
		 * 01001011 // invert
		 * 01001100	// +1 => 76
		 * 
		 * 10110100 => -76
		 */
		
		// how to convert decimal to binary
		// wiki float number 32 precision (single-precision)
		// double number 64 precision (double-precision)
		
		b=-1;
		/*
		 * 00000001
		 * 11111110
		 * 11111111
		 */
		System.out.println();
	}
}
