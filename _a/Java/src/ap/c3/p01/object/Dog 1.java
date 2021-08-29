package ap.c3.p01.object;

// Class
// function
// Class = data + functions (methods)


public class Dog {
	
	// data (properties)
	public String name;
	public int age;
	
	// function (methods, behavior)
	public void barking() {
		System.out.println("Dog is barking");
	}
	
	public String getInfo() {
		return name+" is "+age+" years old";
	}
	
	public static void main(String[] args) {
		Dog dog=new Dog();
		dog.name="Jaja";
		dog.age=10;
		
		System.out.println(dog.getInfo());
		
		dog.barking();
	}
	
}
