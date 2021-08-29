package ap.c07.p01.arrays;

public class UseArray {
	public static void main(String[] args) {
		int[] nums=new int[10];

		for (int i=0;i<10;i++) {
			nums[i]=i*10;
		}
		
		for (int i=0;i<10;i++) {
			System.out.println(nums[i]);
		}
	}
}
