package ap.c09.hashset;

import java.util.Arrays;
import java.util.HashSet;

public class HashSetTest {
	
	// list, set, map
	// set: collection, no order, no position, no duplicate
	
	public static void main(String[] args) {
		HashSet<String> s=new HashSet<String>();
		
		s.add("abc");
		s.add("abc");
		
		String[] i= {"def","xyz"};
		s.addAll(Arrays.asList(i));
		
		System.out.println(s);
		
		//
		Student s1=new Student("Joe",10);
		Student s2=new Student("Joe",10);
		
		HashSet<Student> ss=new HashSet<>();
		ss.add(s1);
		ss.add(s2);
		System.out.println(ss);
		System.out.println(s1==s2); // s1[100], s2[200]
		System.out.println(s1.equals(s2));
		
		System.out.println(s1.hashCode());
		System.out.println(s2.hashCode());
		
		//
		
		System.out.println("###########");
		System.out.println(ss);
		Student s3=new Student("Joe",10);
		System.out.println(ss.contains(s3));

		
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



