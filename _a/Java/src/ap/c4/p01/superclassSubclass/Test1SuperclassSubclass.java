package ap.c4.p01.superclassSubclass;

public class Test1SuperclassSubclass {
	public static void main(String[] args) {
		Dog d = new Dog();
		d.setColor("black");
		
		// inherited
		System.out.println(d.name);
		
		// new data
		System.out.println(d.getColor());
		
		// override
		System.out.println(d.isVegetarian());
	}
}

