package ap.c03.p03.statictest;

public class TestStatic {
	public static void main(String[] args) {
		Dog dog=new Dog("dog");
		System.out.println(dog.getName());
		System.out.println(dog.count);
		
		Dog dog1=new Dog("dog2");
		System.out.println(dog1.count);
	}
}
class Dog{
	private String name;
	public static int count;
	
	public String getName() {
		return name;
	}
	public Dog(String name) {
		count++;
		this.name=name;
		
	}
}