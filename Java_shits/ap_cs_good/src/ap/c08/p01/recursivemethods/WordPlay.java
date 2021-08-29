package ap.c08.p01.recursivemethods;

import java.util.Scanner;

public class WordPlay {
	public static Scanner scanner = new Scanner(System.in);

	public static void stackWords() {
		String word = scanner.nextLine();
		if (word.equals(".")) { // base case
			System.out.println();
		} else {
			stackWords(); // recursive case
		}
		System.out.println(word);
	}

	public static void main(String[] args) {
		System.out.println("enter list of words, one per line:");
		System.out.println("Final word should be a period (.)");
		System.out.println("You will see the words stack together");
		stackWords();
	}
}

// practice: try to print in the input order instead of reversed order?

// recursion method is a method that calls itself
// recursion is a top-down approach to solve a problem

// recursion include 2 parts:
// 1. a base case or more base cases
// 2. a nonbase case that moves towards the base case


