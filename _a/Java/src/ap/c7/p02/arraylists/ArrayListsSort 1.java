
package ap.c7.p02.arraylists;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;

public class ArrayListsSort {
	public static void main(String[] args) {
		// diamond operator
		ArrayList<String> a=new ArrayList<>();
		a.add("Sat");
		a.add("Sun");
		a.add("Mon");
		
		System.out.println(a);
		Collections.sort(a);
		System.out.println(a);
		
		// array
		String[] arr= {"Sat","Sun","Mon"};
		System.out.println(Arrays.toString(arr));
		Arrays.sort(arr);
		System.out.println(Arrays.toString(arr));

	}
}


