package ap.c09.p02.sorts_recursive;

import java.util.Arrays;

/*- split, sort/merge
 * split
 * 5		-3	2	4	0	6
 * 5		-3	2	|	4	0	6
 * 5		-3	|	2	|	4	0	|	6
 * 5		|	-3	|	2	|	4	|	0	|	6
 * 
 * sort and merge
 * -3	5	|	2	|	0	4	|	6
 * -3	2	5	|	0	4	6
 * -3	0	2	4	5	6
 */

/*
 * How to sort and merge?
 * 5	|	6
 * 2	|	4
 * -3	|	0		=> -3
 *
 * 		|	6
 * 5	|	4
 * 2	|	0		=> -3 0
 * 
 * 5	|	6
 * 2	|	4		=> -3 0 2
 * 
 * 		|	6
 * 5	|	4		=> -3 0 2 4
 * 
 * 5	|	6		=> -3 0 2 4 5
 * 	
 * 		|	6		=> -3 0 2 4 5 6
 */
public class Mergesort {
	private static int[] values;
	private static int[] temp;

	private static int numspace;

	public static void sort(int[] vals) {
		values = vals;
		temp = new int[values.length];
		sort(0, values.length - 1);
	}

	private static void printSort(int numspace, int low, int high) {
		int[] a = Arrays.copyOfRange(values, low, high);
		System.out.format("%" + numspace + "s" + "|sort " + low + " " + high + "%n", "");
		System.out.format("%" + numspace + "s" + "|sort " + Arrays.toString(a) + "%n", "");
	}

	private static void printMerge(int numspace, int low, int middle, int high) {
		int[] a1 = Arrays.copyOfRange(values, low, middle);
		int[] a2 = Arrays.copyOfRange(values, middle + 1, high);
		System.out.format("%" + numspace + "s" + "|merge " + low + " " + middle + " " + high + "%n", "");
		System.out.format("%" + numspace + "s" + "|merge " + Arrays.toString(a1) + "%n", "");
		System.out.format("%" + numspace + "s" + "|merge " + Arrays.toString(a2) + "%n", "");
	}

	private static void sort(int low, int high) {
		if (low < high) {
			int middle = low + (high - low) / 2;
			sort(low, middle);
			sort(middle + 1, high);
			mergeHalves(low, middle, high);
		}
	}

	private static void mergeHalves(int low, int middle, int high) {

		// Copy both parts into the helper array
		for (int i = low; i <= high; i++) {
			temp[i] = values[i];
		}

		int i = low;
		int j = middle + 1;
		int k = low;

		// sort and merge
		while (i <= middle && j <= high) {
			if (temp[i] <= temp[j]) {
				values[k] = temp[i];
				i++;
			} else {
				values[k] = temp[j];
				j++;
			}
			k++;
		}

		while (i <= middle) {
			values[k] = temp[i];
			k++;
			i++;
		}
	}

	public static void main(String[] args) {
		int[] vals = { 5, -3, 2, 4, 0, 6 };
		Mergesort.sort(vals);
		System.out.println(Arrays.toString(vals));
	}

}


