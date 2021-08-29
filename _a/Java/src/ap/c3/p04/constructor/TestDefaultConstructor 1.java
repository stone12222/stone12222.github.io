package ap.c3.p04.constructor;

public class TestDefaultConstructor {
	public static void main(String[] args) {
		Dog2 d=new Dog2();
		d.name="Jaja";
		d.age=2;
		System.out.println(d.getInfo());
	}
}

class Dog2{
	String name;
	int age;
	
	// JVM give us a constructor automatically
	// or programmer
	
	// default constructor
	// no parameter
	public Dog2() {
	}
	
	public String getInfo() {
		return name+" is "+age+" years old";
	}
}