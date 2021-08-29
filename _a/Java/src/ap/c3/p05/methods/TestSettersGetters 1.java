package ap.c3.p05.methods;

public class TestSettersGetters {
	// instance == object
	
	public static void main(String[] args) {
		Cat2 c=new Cat2();
		c.setName("Jen");
		System.out.println(c.getName());
		c.setAge(-1);
		System.out.println(c.getAge());
	}
	
	static class Cat2{
		// hide information
		/*-
		 1. don't break other people code
		 2. protect data
		 */
		// control space, control 1, source + generate setter getter
		private String name;
		private int age;
		
		// encapsulation: wrapper hidden information
		public String getName() {
			// logic such as checking id
			return name;
		}
		public void setName(String name) {
			this.name = name;
		}
		public int getAge() {
			return age;
		}
		public void setAge(int age) {
			// check age
			if (age>0) {
				this.age = age;
			} else {
				throw new IllegalArgumentException("Age should large than 0");
			}
			
			/*-
			 how to use it?
			 why we need it? when we should use?
			 and use it to what extent?
			 */
		}	
	}
}

