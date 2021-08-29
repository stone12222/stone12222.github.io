package ap.c7.p02.arraylists;

import java.util.ArrayList;

public class ArrayLists {
	public static void main(String[] args) {
		/*-
		 array: a storage storing a squence of values with same type
		 arraylist: a storage storing a squence of values with same type
		 
		 array: cannot grow 
		 arraylist: can grow
		 
		 */
		// java generics

		// CRUDQ: create, read, update, delete, query
		// create
		ArrayList<Integer> arr=new ArrayList<Integer>();
		arr.add(100);
		arr.add(200);
		arr.add(300);
		System.out.println(arr);
		
		// read
		// index is 0 based
		System.out.println(arr.get(2));
		for (int i=0; i<arr.size(); i++) {
			System.out.println(arr.get(i));
		}
		
		// update
		arr.set(0, 1000);
		System.out.println(arr);
		arr.add(1,3000);
		System.out.println(arr);
		
		// delete
		arr.remove(0);
		System.out.println(arr);
		
		arr.add(200);
		System.out.println(arr);
		arr.remove(new Integer(200));
		System.out.println(arr);
		arr.clear();

		//
		arr.add(200);
		arr.add(100);
		arr.add(100);
		arr.add(100);
		arr.add(100);
		System.out.println("before remove:"+arr);
		
		for (int i=0; i<arr.size(); i++) {
			if (arr.get(i).equals(100)) {
				arr.remove(i);
				i--;
			}
		}
		System.out.println(arr);
		
		// Query 
		System.out.println(arr.size());
		System.out.println(arr.contains(200));

			
	}
}



