package ap.c09.hashmap;

import java.util.HashMap;

public class HashMapTest {
	public static void main(String[] args) {
		HashMap<String, Integer> m=new HashMap<String, Integer>();
		m.put("Joe", 10);
		m.put("John", 10);
		
		System.out.println(m);

		HashMap<Integer, String> map=new HashMap<>();
		map.put(10,"joe");
		String name=map.get(10);
		
		HashMap<String, Student> map2=new HashMap<>();
		map2.put("Joe", new Student("Joe",10));
	}

}

class Student extends Object {
	String name;
	int age;
	
	public Student(String name, int age) {
		this.name=name;
		this.age=age;
	}

	public boolean equals(Object obj) {
		if (obj instanceof Student) {
			Student other=(Student)obj;
			if (this.name.equals(other.name) && this.age==other.age) {
				return true;
			} else {
				return false;
			}
		} else {
			return false;
		}
	};
	
	public int hashCode() {
		return this.age;
	}
}


