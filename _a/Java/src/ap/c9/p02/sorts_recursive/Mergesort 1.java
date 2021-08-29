package ap.c9.p02.sorts_recursive;

import java.util.Arrays;

public class Mergesort {

	static int[] temp;

	public static void main(String[] args) {
		// i mid j
				int[] vals = { 5, -3, 2, 4, 0, 6 };
				sort(vals);
				System.out.println(vals);
	}

	private static void sort(int[] vals) {
		temp = new int[vals.length];
		sort(0, vals.length - 1, vals);
	}

	private static void sort(int i, int j, int[] a) {

		System.out.println("sort: " + Arrays.toString(Arrays.copyOfRange(a, i, j + 1)));
		if (i < j) {
			int mid = (i + j) / 2; // (j-i)/2+i

			// left
			// System.out.println("sort left: " +
			// Arrays.toString(Arrays.copyOfRange(a, i, mid+1)));
			sort(i, mid, a);
			// right
			// System.out.println("sort right: " +
			// Arrays.toString(Arrays.copyOfRange(a, mid + 1, j+1)));
			sort(mid + 1, j, a);

			// merge
			System.out.println("merge: " + Arrays.toString(Arrays.copyOfRange(a, i, j + 1)));
			merge(i, mid, mid + 1, j, a);
		}

	}

	private static void merge(int i, int i1, int j, int j1, int[] a) {

		for (int k = i; k < j1 + 1; k++) {
			temp[k] = a[k];
		}

		int curr=i;
		while (i <=i1  && j<=j1) {
			if (temp[i] < temp[j]) {
				a[curr] = temp[i];
				i++;
			} else {
				a[curr] = temp[j];
				j++;
			}
			curr++;
		}
		// we still have element in the left
		if (i<=i1) {
			while (i<=i1) {
				a[curr]=temp[i];
				i++;
				curr++;
			}
		}
		System.out.println(Arrays.toString(a));

	}
}


