package ap.c3.p02.accesscontrol;

public class UserManager {
	public static void main(String[] args) {
		//
		User user=new User();
		
		//
		System.out.println(user.age);
		System.out.println(user.firstName);
		System.out.println(user.lastName);
		
		// The field User.address is not visible
		// 'access control' controls if we can see it
//		System.out.println(user.address);
		
	}
}
