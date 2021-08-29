package classe.d1.helloWord;


import hsa_ufa.Console;
import java.awt.*; 

public class JavaPrg1 {
   
   public static void main(String[] args) {
      
      Console c = new Console(500,500,15,"Hello, World!");
      
      c.println("Hello, world!");
      c.print("hi1");
      c.println("hi2");
      c.print("hi3",20);
      c.println("hi3");
      c.print("h",20);
      c.println("i");
      c.println(0b1100);
      c.print(1.232,1,2);
      c.println(1.232,10,4);
      c.print(true);
      
   }
   
}