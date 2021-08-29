package ap.c2.p01.packageclass;

import ap.c2.p01.packageclass.testimport.Calculator;

public class TestInput {
	public static void main(String[] args) {
		// create an object from a class
		Calculator cal=new Calculator();
		
		// call object's method
		int result=cal.add(100,200);
		
		System.out.println(result);
	}
}
