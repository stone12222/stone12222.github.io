package ap.c4.p03.ploymorphism;

public class Animal extends Object {
	public void run() {
		System.out.println("Animal can run");
	}

	public void commonBehaviors() {
		System.out.println("Animals common behaviors");
	}

}

/*-
 2 ways to combine object together:
 1. inheritance
 2. composition
 
 2 relationships:
 1. is-a-relation: Cat is a Animal
 2. has-a-relation: Cat has a bell
 */
class Cat extends Animal {
	String name;
	Bell bell;

	@Override
	public void run() {
		System.out.println("Cat run");
	}
}

class Bell {
	
}

class Dog extends Animal {
	public void run() {
		System.out.println("Dog run");
	}

	public void waggingtail() {
		System.out.println("Dog can waggle tail.");
	}

	public void animalRun() {
		super.run();
	}
}



//################################################
class Test {
	
	// for a strong type language, why polymophism?
	/*-
	 if a class has only 1 type, when we deal with the same category types (Cat, Dog, Tiger etc)
	 is there a problem? yes, we need write lots of methdos and it is impossible to do.
	 
	 how to solve? 
	 each class should have more than 1 type (polymophism)
	 then, we can use superclass as reference type
	 */
	
	static void animalRun(Animal d) {
		d.run();
	}

	public static void main(String[] args) {
		Cat c = new Cat();

		c.run();

		/*-
		 2 types:
		 1. real type
		 2. reference type
		 */

		/*-
		 compiler (javac) only care about the reference type
		 but JVM (java) care about the real type
		 */

		/*- Java Virtual Machine
		 how JVM in runtime do binding:
		 - JVM look for the real type and find it is Cat
		 - so bind Cat run() to a
		 */
		Animal a = new Cat();
		a.run();
		System.out.println(a instanceof Cat);
		System.out.println(a instanceof Animal);
		System.out.println(a instanceof Object);

		/*-
		 Cat has 3 types: Cat, Animal, Object
		 we say Cat has Polymophism (multiple types)
		 
		 if a Class or Object has more than 1 type:
		 we say it has Ploymophism
		 */
		
		Test.animalRun(c);
		Test.animalRun(a);
		Test.animalRun(new Dog());
	}
}

/*-
 OO language:
 Inheritance, Encapsulation, Polymorphism
 */




