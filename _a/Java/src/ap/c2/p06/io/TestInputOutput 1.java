package ap.c2.p06.io;

import java.util.Scanner;

public class TestInputOutput {
	
	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		// keyboard > abc > System.in > Scanner
		
		String s=scanner.nextLine();
		System.out.println(s);
		int i=scanner.nextInt();
		System.out.println(i+100);

		// next vs next line
		s=scanner.next();
		System.out.println(s);
		s=scanner.nextLine();
		System.out.println(s);
		// 100
		// 200
		i=scanner.nextInt();
		int j=scanner.nextInt();
		System.out.println(j+i);
		
		// 100 200
		int k=scanner.nextInt();
		int l=scanner.nextInt();
		System.out.println(k+l);
	}
	
}
