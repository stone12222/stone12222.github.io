package ap.c04.p01.superclassSubclass;

//inheritance is for code reuse
//subclass extends superclass
public class Dog extends Animal {

	// reuse superclass code, and add new
	private String color;

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	/* method overriding */
	@Override
	public boolean isVegetarian() {
		return false;
	}
}

class Lab extends Dog {
	
}
