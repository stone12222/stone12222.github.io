package ap.c4.p03.ploymorphism;


public class CallParentOverridenMethod {

	public static void main(String[] args) {
		// upcasting
		Animal d = (Animal)new Dog();
		d = new Dog();
		
		d.run();

		// how to call superclass run()
		((Animal) d).run(); // not work

		// The way to call super method run(), instead of subclass overridden
		// method, such as animalRun() calls super.run();

		// casting is about cast reference type or primitive type 
		// downcasting
		//	d.animalRun(); // not work
		((Dog) d).animalRun();
		
		// Animal is not a Dog, Dog is a Animal 
		// on Runtime, JVM found the animal is not a Dog
		// JVM throw error
		Dog d1=(Dog)new Animal();
//		d1.animalRun();
	}
}

/*-
 		Object
 		  ^
 		  |
		Animal
		  ^
		  |
		Dog
 */
