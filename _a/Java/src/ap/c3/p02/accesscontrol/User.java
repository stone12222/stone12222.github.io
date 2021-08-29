package ap.c3.p02.accesscontrol;

// access control
// public, protected, (package or default), private

// hide information: mainly for maintaining software

public class User {
	// allow access from any classes
	public String firstName="Ashwin";
	protected String lastName="Parapuram";
	
	int age=16;
	
	private String address="London";
	
	// api: application programming interface
	public String getAddress() {
		return address;
	}
	
	public static void main(String[] args) {
		User u=new User();
		
		System.out.println(u.address);
	}
}
