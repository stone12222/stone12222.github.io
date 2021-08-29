package ap.c03.p02.accescontrol.pkg;
import ap.c03.p02.accescontrol.FromItself;

public class FromSubclassOutsidePackage extends FromItself{
	public static void main(String[] args) {
		FromSubclassOutsidePackage c= new FromSubclassOutsidePackage();
//		class
//		System.out.println(c.i);
		
//		package scope
//		System.out.println(c.j);
		
//		protected
		System.out.println(c.k);
		
//		public scope
		System.out.println(c.l);
	}
		
	
}
