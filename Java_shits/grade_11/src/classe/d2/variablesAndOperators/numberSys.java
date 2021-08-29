package classe.d2.variablesAndOperators;

public class numberSys {
	public String tobin(int n) {
		if (n/2!=0) {
			return tobin(n/2)+String.valueOf(n%2);
		} else {
			return "1";
		}
	}
	
	public static void main(String[] args) {
		int x = 101;   // Initialize x to 101^10
		int y = 0101;  // Initialize y to 101^8
		int z = 0x101; // Initialize z to 101^16

		// Print all variables in decimal format
		System.out.println(x);
		System.out.println(y);
		System.out.println(z);

		// Using printf to print all variables in decimal format
		System.out.printf("x=%d y=%d z=%d\n",x,y,z);

		// Using printf to print all variables in octal format
		System.out.printf("x=%o y=%o z=%o\n",x,y,z);

		// Using printf to print all variables in hexadecimal format
		System.out.printf("x=%x y=%x z=%x\n",x,y,z);
		
		//
		numberSys ns=new numberSys();
		int n = 0b110110;
		y = 0267;  
		x = 345;  
		z = 0x3b7d; 
		
		System.out.println(ns.tobin(54));

		System.out.printf("1=%o 1=%d 1=%x\n",n,n,n);

		System.out.printf("2=%o 2=%d 2=%x\n",y,y,y);

		System.out.printf("3=%o 3=%d 3=%x\n",x,x,x);
		
		System.out.printf("4=%o 4=%d 4=%x\n",z,z,z);
		
		
	}
}
