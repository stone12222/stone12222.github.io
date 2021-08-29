package ap.c2.p08.controlflow;

import java.util.ArrayList;
import java.util.Iterator;

/*
AP only test the following unchecked exception
	 ArithmeticException
	 NullPointerException
	 ArrayIndexOutOfBoundsException
	 IndexOutOfBoundsException
	 IllegalArgumentException
	 ConcurrentModificationException
*/

// in python, function
// in java, object=data+function
public class TeztException {
	
	// instance (object) method
	private void divide(int i) {
		System.out.println(100/i);
	}
	
	private void setAge(int age) {
		if (age<=0) {
			 throw new IllegalArgumentException();
		}
		System.out.println(age);
	}
	
	public static void main(String[] args) {
		
		// ArithmeticException
		TeztException te=new TeztException();
//		te.divide(0);
		
		// ArrayIndexOutOfBoundsException
		//          0 1 2 3
		int[] arr= {1,2,3};
//		System.out.println(arr[3]);
		
		// IndexOutOfBoundsException
		ArrayList<Integer> a=new ArrayList<>();
		a.add(100);
		a.add(200);
		a.add(300);
//		System.out.println(a.get(2));
		
		// IllegalArgumentException
//		te.setAge(4);
//		te.setAge(0);
		
		// ConcurrentModificationException
		Iterator<Integer> it=a.iterator();
		while (it.hasNext()) {
			int i=it.next();
			if (i==100) {
//				a.add(100);
//				a.remove(new Integer(100));
//				it.remove();
			}
		}
		
		// nullPointerException
//		Integer i=null;
//		System.out.println(i.intValue());
		
	}
}
