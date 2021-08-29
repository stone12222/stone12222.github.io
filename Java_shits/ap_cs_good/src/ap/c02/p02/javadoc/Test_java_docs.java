package ap.c02.p02.javadoc;

// /** + enter
/**
 * 
 * @author jenniferxu
 *
 */
public class Test_java_docs {
	/**
	 * 
	 * @param str A string to be phrased
	 * @return Integer converted from string
	 * @throws NumberFormatException If string is not a number, throw this exception
	 */
	public int parseInteger(String str) throws NumberFormatException{
			int result=Integer.parseInt(str);
			return result;
	}
}