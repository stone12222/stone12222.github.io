package ap.c03.p07.reference;

public class ReferencesVSPrimitives {
	public static void main(String[] args) {
//		primitive type
		int i=100;
		/*-
		 -------
	i	|  100  |
		 -------
		 */
		
		
//		v is a reference type
//		saves address
		Value v=new Value();
		/*-
		 -------			 --------------
	v	|  100  |  -> 0xFF  | Value Object |
		 -------			 --------------
		 */
	}
}

class Value {
	int i = 100;
}
