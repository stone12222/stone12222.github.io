package ap.c4.p01.superclassSubclass;

// inheritance is for code reuse
// subclass extends superclass

/*-
 child class vs parent class 
 subclass vs superclass
 */
public class Dog extends Animal {
	// reuse superclass code, and add new
	private String color;
	
	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	@Override
	public boolean isVegetarian() {
		return false;
	}
}
// class hierarchy Lab -> Dog -> Animal
class Lab extends Dog {
	
}
