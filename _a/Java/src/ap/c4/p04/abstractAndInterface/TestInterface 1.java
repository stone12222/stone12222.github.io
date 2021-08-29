package ap.c4.p04.abstractAndInterface;

public class TestInterface{
	public static void main(String[] args) {
			Javacode jc= new Javacode();
			jc.readable();
			jc.testable();
	}
}

// interface tells what class can do, with out saying how to do it
// interface is extreme case of abstract class
interface IGoodcode {
	// readable
	void readable();
	// testable
	void testable();
}

abstract class Goodcode implements IGoodcode {
	@Override
	public void readable() {
		System.out.println("code must be readable");
	}
}

class PythonCode extends Goodcode {
	@Override
	public void readable() {
		System.out.println("python code follows google convention");
	}
	
	@Override
	public void testable() {
		System.out.println("the code should be testable");
	}
}

class Javacode implements IGoodcode {
	@Override
	public void readable() {
		System.out.println("Javacode should follow the oreacle convention");
	}
	
	@Override
	public void testable() {
		System.out.println("Javacode should use unit test, intergation ");
	}
}

