package ap.c2.p04.types;

/*-
 final can apply to:
 var

 class
 method
 local var
 */
public final class TestFinalVar {
	
	// instance var
	// final=cannot be changed
	final int LEVEL=3;
	
	public static void main(String[] args) {
		System.out.println(new TestFinalVar().LEVEL);
	}
	
}

//class A extends TestFinalVar3 {
	
//}



