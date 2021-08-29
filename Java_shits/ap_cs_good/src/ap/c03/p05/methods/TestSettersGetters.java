package ap.c03.p05.methods;

public class TestSettersGetters {
	public static void main(String[] args) {
		
		Dog d=new Dog();
		d.setName("");
	}

}

class Dog {
	// Encapsulation
	private String name;
	
	public void setName(String name) {
		// check if name is value
		if (name.length()>0) {
			this.name=name;
		}
	}
	
	public String getName() {
		// check id
		return this.name;
	}
}


