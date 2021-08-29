package ap.c04.p04.abstractAndInterface.copy;


// it is like abstract class, but more lightweight
public interface TestInterface {
//	public abstract String getColor();
	int i=100;
	String getColor();
}

class Sheep implements TestInterface {
	@Override
	public String getColor() {
		return "black";
	}
	
	public static void main(String[] args) {
		Sheep s=new Sheep();
		System.out.println(s.getColor());
		System.out.println(TestInterface.i);
	}
}



