package ap.c2.p08.controlflow;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// Java docs to see Exception, RuntimeException, Error
/*-
	Throwable
	/     \
 Error       Exception
            /         \
"checked exception"		RuntimeException
 IOException etc     	  \
      			        ArithmeticException
*/

/*-
 * 2 ways to handle exception
 * 1. try ... catch
 * 2. throw out
 */

public class TeztHandleException2 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		
		int i=Integer.parseInt(br.readLine());
	}
}
