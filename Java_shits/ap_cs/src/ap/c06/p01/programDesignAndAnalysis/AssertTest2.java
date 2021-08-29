package ap.c06.p01.programDesignAndAnalysis;

public class AssertTest2 {
	public static void main(String[] args) {
		Cat c=new Cat();
		c.setAge(-10);
		System.out.println(c.getAge());
	}
}

class Cat {
	private int age;

	// getter
	public int getAge() {
		return age;
	}

	// setter
	public void setAge(int age) {
		assert age > 0 && age < 200 : "age should between 0 and 200";
		this.age = age;
	}

}


