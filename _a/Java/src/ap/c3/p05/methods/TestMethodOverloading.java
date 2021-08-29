package ap.c3.p05.methods;

public class TestMethodOverloading {
	public static void main(String[] args) {
		Cat cat=new Cat();
		// static binding, run-time binding(lazy binding)
		// static binding is compiler thing
		cat.jump();
		cat.jump(3);
	}
}

class Cat{
	// overloading: same method name with different "type" list for parameter
	public void jump() {
		System.out.println("Cat can jump");
	}
	
	// overloading
	public void jump(int num) {
		System.out.println("Cat can jump "+num+" meters");
	}
	
//	public int jump(int num) {
//		//System.out.println("Cat can jump "+num+" meters");
//		return num;
////	}
	
//	public void jump(int number) {
//		System.out.println("Cat can jump "+number+" meters");
//	}
}