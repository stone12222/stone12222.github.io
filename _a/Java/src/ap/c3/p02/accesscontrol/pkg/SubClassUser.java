package ap.c3.p02.accesscontrol.pkg;

import ap.c3.p02.accesscontrol.User;

public class SubClassUser extends User{
	public static void main(String[] args) {
		User user=new User();
		System.out.println(user.firstName);
		
		SubClassUser u=new SubClassUser();
		System.out.println(u.firstName);
		System.out.println(u.lastName);
	}
	
}
