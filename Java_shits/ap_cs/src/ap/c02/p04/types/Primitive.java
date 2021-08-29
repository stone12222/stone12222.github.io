package ap.c02.p04.types;

public class Primitive {
//8 basic primitives
//	byte, short, int, long; float, double; boolean, char(character)
//	3 tested: int, boolean, double
	
//public = global
	int i;
	boolean b; //true, false
	double d;
	
//	primitives are values, objects are groups of values
	String s;
	
	public static void main(String[] args) {
//		instance=object
//		Primitive --> custom type
		Primitive p=new Primitive();
//		p=primitive
		System.out.println(p.i);
		
		
		
	}
}
