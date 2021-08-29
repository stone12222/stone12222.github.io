package classe.d2.variablesAndOperators;

public class variables {
	public static void main(String[] args) {
		byte b=123;
		int i=111;
		System.out.println(b);
		System.out.println(i);
		System.out.print(Byte.MAX_VALUE);
		System.out.println(Byte.MIN_VALUE);
		System.out.print(Integer.MAX_VALUE);
		System.out.println(Integer.MIN_VALUE);
		System.out.print(Short.MAX_VALUE);
		System.out.println(Short.MIN_VALUE);
		System.out.print(Long.MAX_VALUE);
		System.out.println(Long.MIN_VALUE);
		//
		String text;
		text = "abc123";
		System.out.println("text=" + text);
		//
		int num = 4;
	    System.out.println( "num=" + num );

	    num = 8;
	    System.out.println( "num=" + num );

	    num = num + 1;
	    System.out.println( "num=" + num );
	    //
	    int n=2;
	    System.out.println(n+10);
	    System.out.println(n-10);
	    System.out.println(n*10);
	    System.out.println(n/3);
	    System.out.println(n/3.0);
	    System.out.println((double)n/3);
	    System.out.println(n%3);
	    n=n/3;
	    System.out.println(n);
	    n=10;
	    try {
	    	System.out.println(n/0);
		} catch (Exception e) {
			System.out.println("you got a ArithmeticException since you tried to / by 0");
		}
	    System.out.println(110+(double)32/20*3);
	    System.out.println(0b111000010101);
	    System.out.println(07025);
	    System.out.println(0xe15);
	    System.out.println(0b101101101100);
	    System.out.println(05554);
	    System.out.println(0b110100011110);
	    System.out.println(06436);
	    System.out.println(0xd1e);
	    System.out.println(0xAA1);
	    System.out.println(0b101010100001);

	}
}
