package ap.c09.p01.sorts;

import java.util.Arrays;

/*
8 | 5 2 6 9 3 1 4 0 7
5 8 | 2 6 9 3 1 4 0 7
5 2 8 |
2 5 8 | 6 9 3 1 4 0 7
2 5 6 8 | 9 3 1 4 0 7
2 5 6 8 9 | 3 1 4 0 7
2 5 6 8 3 9
2 5 6 3 8 9
2 5 3 6 8 9
2 3 5 6 8 9 | 1 4 0 7

1. split a collection into sorted list and unsorted list
2. select any one from unsorted list
3. insert the one to the sorted list
*/

public class InsertionSort {
	static void swap(int[] a, int b, int c) {
		int temp = a[b];
		a[b] = a[c];
		a[c] = temp;
	}

//	static void sort(int[] a) {
//		int num = 0;
//		int x = 0;
//
//		while (x == 0) {
//			int n = num;
//			num += 2;
//
//			if ((a[num]) < (a[num - 1])) {
//				swap(a, num, (num - 1));
//
//				if ((num - 1) == 0 || (a[num]) > (a[num - 1])) {
//					x = 1;
//					num=n;
//					System.out.println(Arrays.toString(a));
//				} else {
//					num -= 1;
//					
//				}
//			}
//
//		}
//	}

	static void sort(int[] a) {
		for (int i=1; i<a.length;i+=1) {
			for (int j=i;j>0;j-=1) {
				if (a[j]<a[j-1]) {
					swap(a,j,j-1);
				}
			}
		}
		
	}
	public static void main(String[] args) {
		int[] a = { 8, 5, 2, 6, 9, 3, 1, 4, 0, 7 };
		InsertionSort.sort(a);
		System.out.println(Arrays.toString(a));
	}

}
