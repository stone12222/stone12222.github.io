package ap.c2.p08.controlflow;

public class ForLoop {
	public static void main(String[] args) {
		String s="abc";
		
		// i = 0, 1, 2
		// for loop
		for (int i = 0; i < s.length(); i++) {
			System.out.println(s.charAt(i));
		}
		
		for (char c: s.toCharArray()) {
			System.out.println(c);
		}
		
		// array
		char[] arr= {'a','b','c'};
		
		for (char c: arr) {
			System.out.println(c);
		}
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
		
	}
}
