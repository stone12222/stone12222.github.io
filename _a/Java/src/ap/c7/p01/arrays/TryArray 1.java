package ap.c7.p01.arrays;

import java.util.Arrays;

public class TryArray {
	
	/*
	 multiple choice
	 write code (ccc j2, j3)
	 write code in paper
	 */
	public static void main(String[] args) {
		
		// continuously store 4 zeros in memory, like this: 0 0 0 0
		int[] arr=new int[4];
		System.out.println(arr instanceof Object);

		// declare: define a variable
		int[] a; 
		
		// construct: create an object
		// initialize: populate the array with values
		a=new int[5];
		
		// other ways to create
		float[] b= {1.0f,2,3,4};
		System.out.println(b);
		
		System.out.println(Arrays.toString(b));
		
		// read
		System.out.println(b[2]);

		// update
		b[0]=100;
		System.out.println(Arrays.toString(b));
		
		// cannot delete 
		// by set invalid value
		b[0]=-1;
		System.out.println(Arrays.toString(b));
		
		// by create a new one and make copies
		float[] c=new float[b.length-1];
		c[0]=b[1];
		c[1]=b[2];
		c[2]=b[3];
		
		// 2d
		/*-
		 200 100 1 2 3
		 204 800 4 5
		 208 600 6
		 */
		int[][] i= {{1,2,3},{4,5},{6}};
		int[][] i1=new int[3][];
		i1[1]=new int[3];
		
		//
		double[][] i2;
//		i2= {{1,2,3},{1,2},{1}};
		
//		method({{1,2,3},{1,2},{1}});
		
	}
	
	static void method(double[][] d) {}
	static void method(float[][] d) {}
}

