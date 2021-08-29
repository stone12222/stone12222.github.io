package ap.c04.p04.abstractAndInterface.copy;

public class TestAbstract {
	
	

}

abstract class Animal {
	public void move() {
		System.out.println("Animal can move");
	}
	
	// it creates a contact for its future subclasses
	abstract public String getColor();
}

abstract class Canine extends Animal {
	
}

class Dog extends Canine {
	@Override
	public String getColor() {
		return null;
	}
}

class Cat extends Animal {
	@Override
	public String getColor() {
		return null;
	}
	
}

