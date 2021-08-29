package ap.c08.p02.writingrecursive;

/*-
fac(n)

if n==1: 1 
if n>1: n*fac(n-1)

fac(5)=5*fac(4)=5*4*fac(3)=5*4*3*fac(2)=5*4*3*2*fac(1)=5*4*3*2*1


 */
public class Factorial {
	static int cal(int n) {
		if (n == 1) {
			return 1;
		} else {
			return n * cal(n - 1);
		}
	}

	public static void main(String[] args) {
		System.out.println(cal(4));
	}
}


