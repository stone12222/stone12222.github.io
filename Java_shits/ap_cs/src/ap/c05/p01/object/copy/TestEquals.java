package ap.c05.p01.object.copy;

public class TestEquals{
	public static void main(String[] args) {
		Jennifer j1=new Jennifer();
		j1.name="jen";
		j1.age=3;
		
		Jennifer j2=new Jennifer();
		j2.name="jen";
		j2.age=3;
		
		System.out.println(j1.equals(j2));
	}
}

class Jennifer extends Object {
	String name;
	int age;
	String school;
	String address;
	
	@Override
	public boolean equals(Object obj) {
		return this.name.equals(((Jennifer)(obj)).name);
	}
}

