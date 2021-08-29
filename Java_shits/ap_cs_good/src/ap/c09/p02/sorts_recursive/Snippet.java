package ap.c09.p02.sorts_recursive;
//package snippet;
//
//public class Snippet {
//	looking at a sorted list
//	for every number, the left part is smaller than the right part
//	
//	=>
//	in a unsorted list, if every number has the above property, the list is sorted
//	such as given a name 'pivot'.
//	
//	=>
//	to sort a list
//	the goal is to make every number a pivot
//	
//	4, 1, 2, 7, 5, -1, 8, 0, 6
//	l						 h
//	|Pivot candidate
//	   i                     j
//	      i
//	         i
//	                      j
//	         swap(i,j) if i<=j
//	4  1  2  0  5  -1  8  7  6
//	         i            j
//	            i  j
//	         swap(i,j) if i<=j
//	4  1  2  0 -1   5  8  7  6
//	            i   j
//	        		i
//	        	j
//	         i>j now begin insert pivot candidate to right position to make it real pivot
//	-1 1  2  0  4   5  8  7  6
//			 split list to 2 parts by the pivot
//			 make pivot for both side
//	[-1 1 2 0] and [5 8 7 6]
//	
//	
//	
//}
//
