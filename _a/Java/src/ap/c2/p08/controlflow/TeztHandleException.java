package ap.c2.p08.controlflow;

// Java docs to see Exception, RuntimeException, Error
/*-
	Throwable
	/     \
 Error       Exception
            /         \
"checked exception"		RuntimeException
      	         		   \
      			        ArithmeticException
*/

/*-
 * 2 ways to handle exception
 * 1. try ... catch
 * 2. throw out
 */

public class TeztHandleException {
	
	// no error, when compile time (javac)
	// but get error, when runtime (java)
	private Double divide(int i) {
//		try {
			return (double)(100/i);
//		} catch (ArithmeticException ex) {
//			System.out.println("Exception happened, you need give a non-zero value");
//			return null;
//		}
	}
	
	public static void main(String[] args) {
		TeztHandleException t=new TeztHandleException();
		
		try {
			System.out.println(t.divide(0));
		} catch (Exception ex) {
			System.out.println(ex);
		}
		
		System.out.println("Survival");
	}
}
