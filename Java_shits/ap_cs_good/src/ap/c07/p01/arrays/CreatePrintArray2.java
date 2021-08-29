package ap.c07.p01.arrays;

import java.util.Arrays;

public class CreatePrintArray2 {
	public static void main(String[] args) {
		
		//
		int[] a=new int[5];
		a[0]=100;
		a[1]=200;
		a[2]=300;
		a[3]=400;
		a[4]=500;
		
		System.out.println(Arrays.toString(a));
		
		//
		Integer[] aa=new Integer[2];
		
		String[] s=new String[5];
		double[] d=new double[2];

		//
		int[][] ii=new int[2][];
		ii[0]=new int[3];
		ii[1]=new int[4];
		/*-
		 _ _ _
		 _ _ _ _ 
		 */
		ii[0][0]=100;
		ii[0][1]=200;
		ii[0][2]=300;
		ii[1][0]=400;
		ii[1][1]=500;
		ii[1][2]=600;
		ii[1][3]=700;
		
		//
		int[][] iii= {{1,2,3},{1,2,3,4}};

	}
}


