package ap.c07.p01.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class DeleteList {
	public static void main(String[] args) {
		Integer[] i= {1,1,1,2,2,3};
		ArrayList<Integer> a=new ArrayList(Arrays.asList(i));
		
		// remove by index or by content
		//	a.remove(new Integer(2));
		//	System.out.println(a);
		//
		
		/*
		for (int e:a) {
			if (e==1) {
				a.remove(new Integer(1));
			}
		}
		System.out.println(a);
		*/
		
		// 1,1,1,2,2,3
		//            ^
		// verbose
		Iterator<Integer> iter=a.iterator();
		while (iter.hasNext()) {
			if (iter.next()==1) {
				iter.remove();
			}
		}
		System.out.println(a);
	}
}

