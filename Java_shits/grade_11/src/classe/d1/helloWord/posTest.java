package classe.d1.helloWord;

import hsa_ufa.Console;
import java.awt.*; 

public class posTest {
	public static void main(String[] args) {
		 Console c = new Console(500,500,15,"Hello, World!");
	      
	      c.print("This Console has ");
	      c.print(c.getNumRows());
	      c.print(" rows and ");
	      c.print(c.getNumColumns());
	      c.print(" columns.");
	      c.setCursor(5, 10);
	      c.println("Hello, world!");
	      c.print("The cursor is now on row ");
	      c.print(c.getRow());
	      c.print(" and column ");
	      c.print(c.getColumn());
	      c.print(".");
	      
	      Console c2 = new Console();
	      
	      c2.println("Window 2");
	}
}
