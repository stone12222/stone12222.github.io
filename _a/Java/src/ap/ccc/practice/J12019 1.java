package ap.ccc.practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
10
3
7
8
9
6

7
3
0
6
4
1
 */

public class J12019 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		
		int apple=Integer.parseInt(br.readLine())*3+Integer.parseInt(br.readLine())*2+Integer.parseInt(br.readLine());
		int banana=Integer.parseInt(br.readLine())*3+Integer.parseInt(br.readLine())*2+Integer.parseInt(br.readLine());
		if (apple>banana) System.out.println("A");
		else if (apple<banana) System.out.println("B");
		else System.out.println("T");
	}
}
