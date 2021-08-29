package ap.ccc.practice;

import java.util.Scanner;

/*
3
1
0
 */

public class J12020 {
	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		if (scanner.nextInt()+2*scanner.nextInt()+3*scanner.nextInt()<10) 
			System.out.println("sad");
		else 
			System.out.println("happy");
	}
}
