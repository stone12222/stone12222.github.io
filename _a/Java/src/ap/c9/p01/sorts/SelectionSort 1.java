package ap.c9.p01.sorts;

import java.util.Arrays;

/*-
0 1 2 3 4 5 6 7 8 9 

8, 5, 2, 6, 9, 3, 1, 4, 0, 7
                        ^
i                       j
0, 5, 2, 6, 9, 3, 1, 4, 8, 7
   i              j
0, 1, 2, 6, 9, 3, 5, 4, 8, 7
      ij
0, 1, 2, 6, 9, 3, 5, 4, 8, 7
         i     j
0, 1, 2, 3, 9, 6, 5, 4, 8, 7
            i        j
0, 1, 2, 3, 4, 6, 5, 9, 8, 7
               i  j
0, 1, 2, 3, 4, 5, 6, 9, 8, 7
                  ij
0, 1, 2, 3, 4, 5, 6, 9, 8, 7
                     i     j
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                        ij
*/

// select smallest one
// insertionSort vs selectionSort
/*-
 insertionSort: get an element from unsorted part and carefully insert into sorted part
 selectionSort: carefully select an element and put it into the end of sorted part
 */
public class SelectionSort {
	
	public static void main(String[] args) {
		int[] a= {8, 5, 2, 6, 9, 3, 1, 4, 0, 7};
		sort(a);
		System.out.println(Arrays.toString(a));
	}

	private static void sort(int[] a) {
		int i,j;
		for (i=0; i<a.length-1; i++) {
			// find smallest
			int smallest=a[i];
			int smallestPos=i;
			for (j=i; j<a.length; j++) {
				if (a[j]<smallest) {
					smallestPos=j;
					smallest=a[j];
				}
			}
			
			// swap i and smallestPos
			int t=a[smallestPos];
			a[smallestPos]=a[i];
			a[i]=t;
			System.out.println(Arrays.toString(a));
		}
	}

	
}



