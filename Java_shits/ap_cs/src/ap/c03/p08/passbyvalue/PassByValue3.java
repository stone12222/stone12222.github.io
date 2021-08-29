package ap.c03.p08.passbyvalue;

public class PassByValue3 {
	int add(int i) {
		i=100+i;
		return i;
	}
	
	void add(ZZZ abc) {
		abc.i=abc.i+100;
	}
	
	public static void main(String[] args) {
		PassByValue3 p=new PassByValue3();
		int i=100;
		i=p.add(i);
		System.out.println(i);
		
		//
		ZZZ z= new ZZZ();
		z.i=100;
		p.add(z);
		System.out.println(z.i);
		
	}
}

class ZZZ {
	int i = 100;
}


