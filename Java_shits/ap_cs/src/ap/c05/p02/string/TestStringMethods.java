package ap.c05.p02.string;

public class TestStringMethods {
	public static void main(String[] args) {
		System.out.println("abc".length());
		// index must be in the range
		System.out.println("0123456".substring(1));
		System.out.println("0123456".substring(1, 3));
		//
		System.out.println("0123456".indexOf('3'));
		System.out.println("01234563".indexOf('3', 4));
		System.out.println("01234563".indexOf("345"));
		//
		System.out.println("abc".charAt(1));
	}
}


