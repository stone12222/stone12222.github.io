package ap.c03.p02.accescontrol;

public class FromItself {
//private, package, protected, public
	
//	private variable are only visible in class itself.
	private int i=100;
	
//	package scope is visible in package
	int j=200;
	
//	protected var visible in subclass outside of package
	protected int k=300;
	
//	public var visible anywhere long as you can reference class
	public int l=400;
	
	public static void main(String[] args) {
		FromItself fromItself=new FromItself();
		System.out.println(fromItself.i);
	}
}
class T {
//	private var out of class will not be visible
//	int i=new FromItself().i;
	
	
	int i=new FromItself().j;
}