package ap.c3.p03.statictest;

public class TestStatic {
	
	/*-
	 static:
	 allow use member without creating new object
	 static member is in class level
	 */
	public static void main(String[] args) {
		// access member by class name
		Dog.barking();
		
		//
//		Dog labrador=new Dog();
//		labrador.color="Black";
//		System.out.println(labrador.numberOfEyes);
//		labrador.barking(); // not recommend
//		
//		Dog goldenRetrive=new Dog();
//		goldenRetrive.color="Golden";
//		System.out.println(labrador.numberOfEyes);
//		goldenRetrive.barking();
//		
//		goldenRetrive.numberOfEyes=3;
//		System.out.println(labrador.numberOfEyes);
	}
}

class Dog {
	String color;
	static int numberOfEyes=2;
	
	static void barking() {
		System.out.println("Dog is barking");
	}
	
}
