package ap.c3.p04.constructor;

public class TestThis {
	public static void main(String[] args) {
		Dog3 d=new Dog3("jaja",2);
		System.out.println(d.getInfo());
		
		Dog3 d1=new Dog3("jaja",2);
		System.out.println(d1.getInfo());
	}
}

class Dog3{
	private String name;
	private int age;
	
	
	public Dog3(String name, int age) {
		this.name=name;
		this.age=age;
	}
	
	public String getInfo() {
		System.out.println(this);
		return name+" "+age+" years old";
	}
}
/*-
 in constructor, 'this' means an new empty object.
 in method, 'this' refer to the current object who calls the method.
*/