package ap.c04.p01.superclassSubclass;


public class TestSuperclassSubclass {
	public static void main(String[] args) {
		Dog d = new Dog();

		// public/protected field can be inherited
		// inherit variable
		
		
		
//		System.out.println(d.vegetarian);
		
		
		
		// inherit methods
		System.out.println(d.isVegetarian());

		// can't inherit private var in Animal
		// System.out.println(d.type);
	}
}
