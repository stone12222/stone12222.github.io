package ap.c2.p02.javadoc;

/**
 * @author oggog
 * @version 1.0
 * @since 2021
 * 
 * This class shows how to write javadocs
 * 
 */
public class TestJavaDocs extends Object{
	/**
	 * java is string typed language
	 */
	String name;
	int age;
	
	/**
	 * 
	 * @param name is a people name
	 */
	public void setName(String name) {
		this.name = name;
	}
	
	/**
	 * @return a sting representation of the object
	 */
	public String toString() {
		return name+" "+age+" years old";
	}
	
}
