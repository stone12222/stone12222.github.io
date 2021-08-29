package ap.c3.p07.reference;

public class ReferencesVSPrimitives {
	public static void main(String[] args) {
		int i=100;
		/*-
		  -----
	i    | 100 |
		  -----
		 */
		
		// v is reference type
		Value v=new Value();
	/*-
	 	 ------          ----------
	 v  | 0xFF | -> 0xFF | Object |
	     ------          ----------
	 */
	}
}

class Value {
	int i = 100;
}
