package ap.c5.p02.string;

public class TestString {

	public static void main(String[] args) {
		// string are constants
		// string is immutable (not changed)
		
		String s1 = "abc";
		String s2 = "abc";

		System.out.println(s1 = s2);
		System.out.println(s1.equals(s2));

		//
		s1 = new String("abc");
		s2 = new String("abc");
		System.out.println(s1 == s2);
		System.out.println(s1.equals(s2));
		
		// == not reliable
		// usually use .equals
		
		/*-
		 String value cannot be changed
		 but string variable can be changed
		 */
		s2="abc";
		s2=s2.replace("a", "d");
		System.out.println(s2);
	}
}
