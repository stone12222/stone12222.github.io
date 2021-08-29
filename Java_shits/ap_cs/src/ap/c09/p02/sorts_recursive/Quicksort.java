package ap.c09.p02.sorts_recursive;

import java.util.Arrays;

/*-
[-1, 0, 2, 4, 4, 5, 6, 7, 8]

4, 4, 2, 7, 5, -1, 8, 0, 6
|pivot candidate
   i                     j
         i            j
4, 4, 2, 0, 5, -1, 8, 7, 6
            i   j
4, 4, 2, 0,-1,  5, 8, 7, 6
                i
            j
-1, 4, 2, 0,4,  5, 8, 7, 6
			|pivot
 */

public class Quicksort {
	private static int[] values;

	public static void sort(int[] vals) {
		values = vals;
		sort(0, values.length - 1);
	}

	private static void sort(int low, int high) {
		if (low < high) {
			int pivot = values[low];
			int i = low + 1, j = high;

			while (i < j) {
				// while (values[i] <= pivot && i <= j) {
				// note: I have to put i<=j before values[i]<=pivot, otherwise, I got index
				// error
				while (i <= j && values[i] <= pivot) {
					i++;
				}

				while (values[j] >= pivot && j >= i) {
					j--;
				}

				if (i <= j) {
					swap(i, j);
				}
				System.out.println(Arrays.toString(values));
			}

			if (i>j) {
				swap(low, j);
				System.out.println(Arrays.toString(values));
			}
			sort(low, j - 1);
			sort(j + 1, high);
		}
	}

	private static void swap(int i, int j) {
		int temp = values[i];
		values[i] = values[j];
		values[j] = temp;
	}

	public static void main(String[] args) {
		int[] values = { 4, 4, 2, 7, 5, -1, 8, 0, 6 };
		System.out.println(Arrays.toString(values));
		Quicksort.sort(values);
		System.out.println(Arrays.toString(values));
	}
}


