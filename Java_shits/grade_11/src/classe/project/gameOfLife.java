package classe.project;

import java.awt.Color;
import java.awt.event.MouseEvent;

import hsa_ufa.Console;

public class gameOfLife {
	
	public static void main(String[] args) {
		Console c=new Console(900,600,20,"Conway's Game of Life");
		main_menu mm=new main_menu(c);
		mm.display();
	
	}
}


/*-
The interfaces abstract class are the parent class of all graphic
related class. Method with in the class are likely going to be 
overridden in other class
 */
abstract class interfaces{
	Console c;
	public final int Max_Width=900;
	public final int Max_Height=600;
	button[] buttons;
	
	public interfaces(Console consleUsing) {
		c=consleUsing;
	}
	
	/*-
	This method will setup an array of button object.
	arrs is a 2d array and which array must have 4 element.
	each element represent the x, y, width and height of the 
	button.
	texts are a array of String that represents the text you 
	want to have on each button.
	c are for the console object so each it is using the same 
	console object rather then creating a new one every time
	 */
	public void setUpButtons(int[][] arrs,String[] texts) {
		buttons=new button[arrs.length];
		for (int i = 0; i < arrs.length; i++) {
			buttons[i]=new button(arrs[i][0],arrs[i][1],arrs[i][2],arrs[i][3],texts[i],c);
		}

	}
	
	/*-
	 this display method will display all buttons,
	 it is being overridden in other class.
	 */
	public void display() {
		for (int i = 0; i < buttons.length; i++) {
			buttons[i].displayButton();
		}
	}
}


class button{
	private int x;
	private int y;
	private int width;
	private int height;
	private String text;
	private boolean pressed=true;
	Console c;
	
	public button(int x, int y,int width, int height,String text,Console consleUsing) {
		this.x=x;
		this.y=y;
		this.width=width;
		this.height=height;
		this.text=text;
		c=consleUsing;
	}
	
	/*-
	this private method help to determine the position of the text
	with in the button so that it is in the middle of it.
	 */
	private int[] computTextPos(int width, int height) {
		int buttonHeightMid=(int)(height/2+0.5+y);
		int buttonWidthMid=(int)(width/2+0.5+x);
		
		int textPosx=(int)(buttonHeightMid-text.length()*11.5/2+0.5);
		int textPosy=buttonHeightMid-9;
		
		int[] pos={textPosx,textPosy};
		return pos;
	}
	
	public void displayButton() {
		c.setColor(Color.white);
		c.fill3DRect(x, y, width, height, pressed);
		if (pressed) {
			c.setColor(Color.green);
			c.fill3DRect(x, y, width, height, pressed);
		} else {
			c.setColor(Color.red);
			c.fill3DRect(x, y, width, height, pressed);
		}
	}
	
//	public boolean isPressed() {
//		c.getMouseClick();
//	}
}


/*-
 the class are used when the user are on the main menu
 it is a sub class of interface, it inherits all the none
 private thing in interface
 */
class main_menu extends interfaces{
	public main_menu(Console consleUsing) {
		super(consleUsing);
		int[][] buttonsPosAndSize={{390,360,120,30},{390,410,120,30},{390,460,120,30}};
		String[] texts= {"hi","hi","hi"};
		setUpButtons(buttonsPosAndSize, texts);
	}
	
	/*-
	 this overrides the method in interfaces
	 it display the button but it also has display this
	 that only main_menu has
	 */
	public void display() {
		super.display();
	}
}
