package ap.c04.p04.abstractAndInterface.copy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TestComparable {
	public static void main(String[] args) {
		Cow c=Cow.createCow();
		c.weight=200;
		c.color="red";		

		Cow c1=Cow.createCow();
		c1.weight=100;
		c1.color="black";
		
		List<Cow> l=new ArrayList<Cow>();
		l.add(c);
		l.add(c1);
		System.out.println(l);
		
	    //
		Collections.sort(l);
		System.out.println(l);
	}
}

class Cow implements Comparable<Cow>{
	double weight;
	String color;
	
	private Cow(double w, String c) {
		weight=w;
		color=c;
	}
	
	public static Cow createCow() {
		return new Cow(0,"black");
	}

	@Override
	public int compareTo(Cow c) {
//		if (this.weight<c.weight) {
//			return -1;
//		} else if (this.weight==c.weight) {
//			return 0;
//		} else {
//			return 1;
//		}
		
		return this.color.compareTo(c.color);
	}
	
	@Override
	public String toString() {
		return "("+this.weight+" "+this.color+")";
	}
}




