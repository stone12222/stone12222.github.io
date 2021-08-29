package course.graph;

import java.util.*;

//use LinkedList in an array to represent Adjacency list
public class DFS2_recursion {
	static class Graph {
		private int V; // No. of vertices
		private LinkedList[] adj; // Adjacency Lists

		// Constructor
		Graph(int v) {
			V = v+1;
			adj = new LinkedList[V];
			for (int i = 0; i < V; ++i)
				adj[i] = new LinkedList<Integer>();
		}

		void addEdge(Integer v, Integer w) {
			adj[v].add(w);
			adj[w].add(v);
		}

		void dfs(int s) {
			boolean[] visited = new boolean[V];
			dfs(s,visited);
			System.out.println(Arrays.toString(visited));
		}

		void dfs(int s, boolean[] visited) {
			if (visited[s]==false) {
				visited[s]=true;
			}
			System.out.println(s);

			LinkedList<Integer> neighbours=adj[s];
			for (int n:neighbours) {
				if (!visited[n]) {
					dfs(n,visited);
				}
			}
		}
	}

	// Driver method to
	public static void main(String args[]) {
		Graph g = new Graph(6);
		g.addEdge(1, 2);
		g.addEdge(1, 3);
		g.addEdge(2, 4);
		g.addEdge(2, 5);
		g.addEdge(3, 6);
		g.addEdge(5, 6);
		g.dfs(1);
	}
/*-
  1
 / \
2   3
/ \   \
4   5 - 6
*/
}


