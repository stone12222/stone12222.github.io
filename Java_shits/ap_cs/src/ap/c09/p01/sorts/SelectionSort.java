package ap.c09.p01.sorts;

import java.util.Arrays;
/*
[][8 5 2 6 9 3 1 4 0 7]
[0] [5 2 6 9 3 1 4 8 7]  #1
[0 1] [2 6 9 3 5 4 8 7]  #2
[0 1 2] [6 9 3 5 4 8 7]
[0 1 2 3] {9 6 5 4 8 7]
[0 1 2 3 4] [6 5 9 8 7]
[0 1 2 3 4 5] [6 9 8 7]
[0 1 2 3 4 5 6] [7 8 9]
[0 1 2 3 4 5 6 7] [8 9]
[0 1 2 3 4 5 6 7] [8 9]  #9

search-and-put-at-end-of-the-list algorithm
*/

public class SelectionSort {
	static void swap(int[] a, int b, int c) {
		int temp = a[b];
		a[b] = a[c];
		a[c] = temp;
	}

	static void sort(int[] a) {
		int j;
		int k;
		j=a.length-1;
		k=a[a.length-1];
		
		for (int i = 0; i < a.length; i += 1) {
			if (a[i]<k) {
				j=i;
				k=a[i];
			}
			swap(a,j,a[1]);
		}

	}

	public static void main(String[] args) {
		int[] a = { 8, 5, 2, 6, 9, 3, 1, 4, 0, 7 };
		SelectionSort.sort(a);
		System.out.println(Arrays.toString(a));
	}

}
