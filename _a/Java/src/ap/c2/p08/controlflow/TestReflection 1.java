package ap.c2.p08.controlflow;

import java.lang.reflect.Method;

public class TestReflection {
	public static void main(String[] args) {
		// in runtime, how to find information from a class
		Integer i;
		Method[] methods = Integer.class.getMethods();
		System.out.println(methods[2].getName());
		
	}
}
