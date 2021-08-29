package ap.c2.p06.io;

import java.util.Scanner;

public class IOExample {
	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		
		/*
		 5
		 100 200
		 5 6
		 7 8
		 10 20
		 30 40
		 */
		int ans=0;
		int j=scanner.nextInt();
		for (int i=0; i<j; i++) {
			ans+=scanner.nextInt();
		}
		System.out.println(ans);
	}
}