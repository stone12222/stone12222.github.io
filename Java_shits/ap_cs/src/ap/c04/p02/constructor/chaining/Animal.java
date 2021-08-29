package ap.c04.p02.constructor.chaining;

public class Animal {
	
	protected int age; // hiding information 

	public Animal(int age) {
		this.age=age;
	}

	public static void main(String[] args) {
		Dog d=new Dog("Jaja", 10);
		System.out.println(d.getAge());
	}
}


class Dog extends Animal {
	private String name;
	
	public int getAge() {
		return age;
	}
	
	public Dog(String name, int age) {
		super(age);
		this.name=name;
	}
}

