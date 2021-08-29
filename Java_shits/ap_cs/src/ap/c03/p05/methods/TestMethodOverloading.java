package ap.c03.p05.methods;

public class TestMethodOverloading {
	public static void main(String[] args) {


	}

}

class Dog1 {
	int height = 1;

	// valid method overloading:
//	method names are the same, but with different parameter type list. 
	public void jump() {
		System.out.println("Cat jumps " + height + " meters");
	}

	// Formal parameter 'height'
	public void jump(int height) {
		System.out.println("Cat jumps " + height + " meters");
	}
	
	
//	can not tell which one to call
//	public boolean jump(int height) {
//		return height<5;
//	}
}


