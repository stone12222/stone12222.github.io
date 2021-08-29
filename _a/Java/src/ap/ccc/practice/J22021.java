package ap.ccc.practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class J22021 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int people=Integer.parseInt(br.readLine());
		String name="";
		String newName="";
		double amount=0;
		int newAmount=0;
		
		
		for (int i=0; i<people; i++) {
			newName=br.readLine();
			newAmount=Integer.parseInt(br.readLine());
			if (newAmount>amount) {
				amount=newAmount;
				name=newName;
			}
		}
		System.out.println(name);
	}
}

