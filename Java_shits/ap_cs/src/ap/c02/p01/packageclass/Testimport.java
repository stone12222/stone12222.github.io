package ap.c02.p01.packageclass;

import ap.c02.p01.packageclass.testimport.Calculate;

public class Testimport {
	public static void main(String[] args) {
		Calculate c=new Calculate();
		int result=c.add(100, 200);
		System.out.println(result);
	}
}