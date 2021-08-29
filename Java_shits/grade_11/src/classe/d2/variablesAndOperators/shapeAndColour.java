package classe.d2.variablesAndOperators;

import java.awt.Color;
import java.awt.event.MouseEvent;

import hsa_ufa.Console;

public class shapeAndColour {
	public static void main(String[] args) {
		Console c=new Console(500,500,15,"Shapes");
	      c.print("The Console is " + c.getDrawWidth() + " pixels wide ");
	      c.println("and " + c.getDrawHeight() + " pixels high.");
	      c.setColor(Color.red);
	      c.drawLine(50, 30, 200, 30);
	      c.drawRect(0, 35, 40, 40);
	      c.fillRect(45, 35, 40, 40);
	      c.drawRoundRect(90, 35, 40, 40, 15, 15);
	      c.fillRoundRect(135, 35, 40, 40, 10, 10);
	      c.draw3DRect(180,35, 40, 40, false);
	      c.fill3DRect(225, 35, 40, 40, true);
	      c.drawOval(270, 35, 40, 40);
	      c.fillOval(315, 35, 40, 40);
	      c.drawArc(360, 35, 40, 40, 30, 300);
	      c.fillArc(405, 35, 40, 40, -120, 200);
	      c.drawStar(450, 35, 40, 40);
	      c.fillStar(0, 80, 40, 40);
	      c.drawMapleLeaf(45, 80, 40, 40);
	      c.fillMapleLeaf(90, 80, 40, 40);
	      //
	      int x[] = { 250, 270, 290, 280, 290, 270, 250, 260 };
	      int y[] = {80,   90,  80,  100,  120,  110,  120,  100 };

	      c.drawPolygon(x, y, 8);
	      for (int i = 0; i < 8; i++)
	         x[i] += 50;
	      c.fillPolygon(x, y, 8);
	      
	      c.drawRect(-10, 200, 60, 60);
	      
	      while(true) {
	    	  System.out.println(c.getMouseX());
	    	  System.out.println(c.getMouseY());
	      }
	}
}
