package ap.c02.p08.controlflow;


import java.util.ArrayList;

//AP only test the following unchecked exception
//ArithmeticException
//NullPointerException
//ArrayIndexOutOfBoundsException
//IndexOutOfBoundsException
//IllegalArgumentException



import java.util.Arrays;
import java.util.List;

public class TestException {
	
	static int i=100;
	int age;
	
	public int divide(int n) {
		return i/n;
	}
	
	public void setAge (int age) {
		if (age<=0) {
			throw new IllegalArgumentException();
		}
		this.age=age;
	}
	
	public static void main(String[] args) {
		TestException e=new TestException();
//		e.divide(0);
		
		String s=null;
//		System.out.println(s.length());
		
		
//		
		int[] i={1,2,3};
		System.out.println(Arrays.toString(i));
//		System.out.println(i[4]);
		
		
//		
		List<Integer> a=new ArrayList<Integer>();
//		System.out.println(a.get(2));
		
//		to handle the error
		try{
			e.setAge(-1);
		}catch(IllegalArgumentException ex) {
			System.out.println(ex);
		}
//		e.setAge(-1);
		
		/*-
		  Throwable
			/     \
		 Error       Exception
		            /         \
		"checked exception"		RuntimeException
		      	         		   \
		      			        ArithmeticException
		 */
	}
}
