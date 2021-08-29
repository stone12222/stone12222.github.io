package ap.c07.p01.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

/*
ArrayList implements List
1. is like array
2. but can grow
3. more apis such as search, sort etc
*/
public class Arraylist {
	String name;
	
	public static void main(String[] args) {
		Integer[] i= {1,2,3};
		ArrayList<Integer> a=new ArrayList<>(Arrays.asList(i));
		a.add(100);
		a.add(200);
		System.out.println(a);

		a.add(a.size(),300);
		System.out.println(a);
		
		System.out.println(a.contains(1));

		// get
		int j=a.get(2);
		// set
		a.set(3, 3000);

		System.out.println(a);
		
		// sort
		Collections.sort(a);
		
		// loop
		for (int k=0; k<a.size(); k++) {
			System.out.println(a.get(k));
		}
		//
		int l=0;
		while (l<a.size()) {
			System.out.println(a.get(l));
			l++;
		}
		//
 		for (Integer e: a) {
			System.out.println(e);
		}
		// Iterator
		// 1,2,3
		// ^
		Iterator<Integer> iter=a.iterator();
		while (iter.hasNext()) {
			System.out.println(iter.next());
		}
		a.clear();
	}
}


