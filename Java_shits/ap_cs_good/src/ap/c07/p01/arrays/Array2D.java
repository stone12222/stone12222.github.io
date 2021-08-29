package ap.c07.p01.arrays;

import java.util.Arrays;

public class Array2D {
	public static void main(String[] args) {
		int[][] a = {
				{ 1, 3, 5, 7 },
				{ 2, 4, 6, 8 },
				{ 3, 5, 7, 9 }
		};

		/*-
		1357
		2468
		3579
		
		3577
		4688
		5799
		 */
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				System.out.print(a[i][j]);
			}
			System.out.println();
		}
	}

}

