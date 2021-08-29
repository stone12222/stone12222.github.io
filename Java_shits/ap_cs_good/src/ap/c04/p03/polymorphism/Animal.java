package ap.c04.p03.polymorphism;

public class Animal {
	public void run() {
		System.out.println("Animal run");
	}
	
	public static void animalRun(Animal a) {
		a.run();
	}
	
	public static void main(String[] args) {
		// d object has 2 types: Animal and dog
		// if an object has more than 1 type, it is a polymorphism
		Animal d=new Dog();
		d.run();
		
		// is-a: 
		// dog is a animal, dog is a dog, dog is an object
		System.out.println(d instanceof Animal);
		System.out.println(d instanceof Dog);
		System.out.println(d instanceof Object);
		
		animalRun(d);
		
		Cat c=new Cat();
		animalRun(c);
	}
}

class Dog extends Animal {
	public void run() {
		super.run();
		System.out.println("Dog run");
	}
	
	public void bark() {
		System.out.println("Dog bark");
	}
}
class Cat extends Animal {
	public void run() {
		System.out.println("Cat run");
	}
}
