package ap.c2.p06.io;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class TestInputOutput2 {
	
	public static void main(String[] args) throws NumberFormatException, IOException{
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		
/*-
5
100 200
5 6
7 8
10 20
30 40
*/
		
		int n=Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			StringTokenizer st =new StringTokenizer(br.readLine());
			int j=Integer.parseInt(st.nextToken());
			int k=Integer.parseInt(st.nextToken());
			System.out.println(j+k);
		}
	}	
}
