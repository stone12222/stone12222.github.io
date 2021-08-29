package ap.c03.p03.statictest;

//1. java VM finds and load class to memory. At that time, static members are already available. 
//2. you can create objects from the class. 

//instance var VS static var


public class TestStatic2 {
//	**Static member can be shared by objects**
//	static member belongs to the Class, so the static var is not an instance variable.
	
//	static makes accessing class member easier
//	static makes tracking number of objects possible
	public static void main(String[] args) {
//		Dog1 dog1=new Dog1("Jaja");
//		Dog1.count=100;
//		dog1.count=100;
		
		
//		Dog1 dog2=new Dog1("Jaja");
//		Dog2.count=200;
//		dog2.count=200;
		System.out.println(Dog1.count);
		

//		static member is available before the object created
	}
}

class Dog1 {
	private String name;
	public static int count;
	
	public String getName() {
		return name;
	}
	
	public Dog1(String name) {
		this.name=name;
	}
}

