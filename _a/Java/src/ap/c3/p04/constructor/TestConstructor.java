package ap.c3.p04.constructor;

public class TestConstructor {
	public static void main(String[] args) {
		Dog dog=new Dog("Jaja", 2);
		System.out.println(dog.getInfo());
	}
}

class Dog{
	
	private String name;
	private int age;
	
	// use constructor to create object
	// when create object, you need information(parameters)
	public Dog(String name, int age) {
		System.out.println("object is created");
		this.name=name;
		this.age=age;
	}
	
	public String getInfo() {
		return name+" "+age+" years old";
	}
}