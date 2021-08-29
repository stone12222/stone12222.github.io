package ap.c03.p02.accescontrol;

public class FromSamePackage {
	public static void main(String[] args) {
		FromItself c=new FromItself();
//		class
//		System.out.println(c.i);
		
//		package scope
		System.out.println(c.j);
		
//		protected
		System.out.println(c.k);
		
//		public scope
		System.out.println(c.l);
	}
}
