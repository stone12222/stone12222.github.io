package ap.c3.p02.accesscontrol.pkg;

// ctrl-o
import ap.c3.p02.accesscontrol.User;

public class AnotherUserManager {
	public static void main(String[] args) {
		User user=new User();
		
		System.out.println(user.firstName);
		
		// can not see 'protected', 'package', 'private'
		
	}
}
