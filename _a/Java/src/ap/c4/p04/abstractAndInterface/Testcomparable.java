package ap.c4.p04.abstractAndInterface;

public class Testcomparable {
	public static void main(String[] args) {
		
		// primitive vs reference type
		int i1=100;
		int i2=200;
		System.out.println(i1>i2);
		
		Integer i3=i1; // boxing
		Integer i4=i2; 
		
		System.out.println(i3>i4); // unboxing
		
		/*-
		 -1 means i3<i4
		 0 means i3=i4
		 1 means i3>i4
		 */
		System.out.println(i3.compareTo(i4));
		
		//
		String s1="ABC";
		String s2="ABB";
		
		// ABC - ADB
		System.out.println(s1.compareTo(s2));
	}
}
