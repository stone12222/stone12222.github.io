package ap.c03.p02.accescontrol.pkg;

import ap.c03.p02.accescontrol.FromItself;

public class FromClassOutsidePakage {
	public static void main(String[] args) {
		FromItself c=new FromItself();
//		protected is not visible outside of package
//		System.out.println(c.k);
		
//		class
//		System.out.println(c.i);
		
//		package scope
//		System.out.println(c.j);
		
//		protected
//		System.out.println(c.k);
		
//		public scope
		System.out.println(c.l);
	}
}
