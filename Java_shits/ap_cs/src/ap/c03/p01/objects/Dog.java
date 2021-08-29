package ap.c03.p01.objects;

public class Dog {
//	State, properties, data
	String name;
	int age;
	
	
	public Dog(String name, int age) {
		this.name=name;
		this.age=age;
	}
	
//	method
	public void barking() {
		System.out.println("My name is "+name);
	}
	
	public static void main(String[] args) {
		Dog d=new Dog("J",10);
		System.out.println(d.name);
		System.out.println(d.age);
		d.barking();
	}
}
