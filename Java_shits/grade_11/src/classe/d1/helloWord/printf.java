package classe.d1.helloWord;

public class printf {
	public static void main(String[] args) {
		System.out.printf("%d\n",44);        // Print integer
		System.out.printf("%3d\n",44);       // Print integer, but make sure it takes up 3 characters...this will print " 44"
		System.out.printf("%03d\n",44);      // Same as above, but fill with 0s instead of " "s
		System.out.printf("%f\n",4.4);       // Print a decimal number
		System.out.printf("%.2f\n",4.4);     // Print a decimal number with 2 digits after the decimal
		System.out.printf("%8.2f\n",4.4);    // Same as above, but fill left with " "s, enough to make the whole number 8 characters wide
		System.out.printf("%12s %-12s\n", "Team", "City");  // Print text right- or left-aligned, each field is 12 characters wide
		System.out.printf("%04X\n",44);      // Print a hexadecimal number, 4 characters wide, with 0s filling at left
		                                     // We'll learn about hexadecimal numbers, and octal numbers (print with %o)
		                                     // in a future unit.

		System.out.printf("%%\n");           // Print a % sign

		System.out.printf("%10s %4d %4.1f\n", "text", 123, 4.56);  // Print several items at once

		System.out.printf("The answer is %d.\n", 789);  //Print text and numbers another way
	}
}
