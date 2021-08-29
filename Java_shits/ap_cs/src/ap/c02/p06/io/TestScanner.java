package ap.c02.p06.io;

import java.util.Scanner;

//Will not be tested in exam

public class TestScanner {
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		String input=s.next();
		
		System.out.println(input);
		
		int i=s.nextInt();
		System.out.println(i);
		
		
		s.hasNextLine();
		
//		Doesn't read new line character
		String line=s.nextLine();
//		[] array only stores the same type
		String[] i1=line.split("");
		System.out.println(i1[0]);
		System.out.println(i1[1]);
		
	}
}
