package ap.c03.p07.reference;

public class TestThis {
	public static void main(String[] args) {
		// reference object outside of class
		Dog d = new Dog("Jaja");
		System.out.println(d);
		Dog d1 = new Dog("DaHuang");
		d1.printName();
	}
}

class Dog extends Object {
	public String name1;
	public int age;

	public Dog(String name) {
		name1 = name;
	}
	
	public String toString() {
		String s=name1+" is "+age+" years old";
		s+="@"+this.hashCode();
		return s;
	}

	// how to reference current object in Class
	public void printName() {
		// System.out.println(name);
		System.out.println(name1);
		System.out.println(this);
		System.out.println(this);
		System.out.println(this.name1);
	}
}


