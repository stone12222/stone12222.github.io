package ap.c05.p03.wrapperclass;

import java.util.ArrayList;
import java.util.List;

/*-
 byte, char, short, int, long, float, double, boolean
 
 Wrapper class:
 Byte, Character, Short, Integer, Long, Float, Double, Boolean
 */
public class WrapperClass3 {
	public static void main(String[] args) {
		int i=100; // only data

		// boxing
		Integer ii=i; // object hold data

		// unboxing
		int j=ii+100;
		System.out.println(j);
		ii=200;
		
		//
		Integer z=ii+100;
		// unbox ii to 100
		// do 100+100
		// box 200
		
		//
		List<Integer> l=new ArrayList<Integer>(); 
		l.add(100);
		l.remove(0);
		
		//
		char c='a';
		int k=(int)c;
		
		// primitive <-> wrapper
		Integer a=new Integer(100);
		a.intValue();
		
		// String to wrapper
		Integer b=Integer.valueOf("100");
		Integer d=Integer.parseInt("100");
	}
}


