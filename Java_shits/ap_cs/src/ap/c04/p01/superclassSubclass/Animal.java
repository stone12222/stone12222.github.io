package ap.c04.p01.superclassSubclass;

public class Animal {
	private boolean vegetarian = true;
	private String type = "Animal";

	public boolean isVegetarian() {
		return vegetarian;
	}

	public void setVegetarian(boolean vegetarian) {
		this.vegetarian = vegetarian;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	// static method
	public static void run() {
		System.out.println("Animal can run");
	}
}
