package ap.c6.p01.programDesignAndAnalysis;

public class CheckedRuntimeError {
	/*-
		Throwable 
		/       \
	Error		Exception
	(unchecked)	
				/			\ 
			(checked)      RuntimeException 
			               (unchecked)
	 */
	
	void setNumber(int number) throws NumberException {
		if (number>10 && number<100) {
			
		} else {
			throw new NumberException();
		}
	}
	
	public static void main(String[] args) {
		CheckedRuntimeError c=new CheckedRuntimeError();

		/*-
		 2 ways to handle exception:
		 1. try catch
		 2. throws 
		 */
		
		/*-
		 checked exception means you need handle
		 
		 for runtime exception, you don't need handle, but you can
		 */
		try {
			c.setNumber(0);
		} catch (NumberException e) {
			e.printStackTrace();
		}
		
	}
}

class NumberException extends Exception {
	
}


