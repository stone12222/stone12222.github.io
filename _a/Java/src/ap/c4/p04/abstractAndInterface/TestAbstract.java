package ap.c4.p04.abstractAndInterface;

public class TestAbstract {
	
	public static void main(String[] args) {
		// Can we directly create object from abstract class?
		// No. in ap book
		
//		Shape1 s=new Shape1(10,10,100,200) {
//			@Override
//			public double getArea() {
//				return width*height;
//			}
//		};
		
		Rectangle1 rectangle1=new Rectangle1(10, 10, 100, 200);
		System.out.println(rectangle1.getArea());
		
		Square1 square1=new Square1(10, 10, 100);
		System.out.println(square1.getArea());
		
		Circle1 circle1=new Circle1(10,10, 100);
		System.out.println(circle1.getArea());
		
	}
}

// a class have abstract methods =>the class is abstract class
// an abstract class don't neccessary to have abstract methods
abstract class Shape1 {
	int x;
	int y;
	int width;
	int height;
	
	public Shape1(int x,int y, int width, int height) {
		this.x=x;
		this.y=y;
		this.width=width;
		this.height=height;
	}
	
	// method has no body
	public abstract double getArea();
}

class Rectangle1 extends Shape1 {
	public Rectangle1(int x, int y, int width, int height) {
		super(x,y,width,height);
	}
	
	public double getArea() {
		return width*height;
	}
}

class Square1 extends Rectangle1 {
	int size;
	
	public Square1(int x,int y, int size) {
		super(x,y,size,size);

		this.size=size;
	}
}

class Circle1 extends Square1 {
	
	public Circle1(int x,int y, int radius) {
		super(x,y,radius);
	}
	
	@Override
	public double getArea() {
		return Math.PI*size*size;
	}
}

