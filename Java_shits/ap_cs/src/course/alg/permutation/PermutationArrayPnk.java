package course.alg.permutation;

import java.util.ArrayList;

public class PermutationArrayPnk {
  public static void process() {
     // System.out.println(Arrays.toString(a));
  }

  static void search(int[] arr, int n, int k, ArrayList<Integer> result) {
     if (result.size() == k) {
        process();
     } else {
        for (int i = 0; i < n; i++) {
           if (arr[i] == 1)
              continue;
           // choose
           arr[i] = 1;
           result.add(i);
           // permute
           search(arr, n, k, result);
           // unchoose
           arr[i] = 0;
           result.remove(result.size() - 1);
        }
     }
  }

  static void permute(int n, int k) {
     ArrayList<Integer> result = new ArrayList<>();
     int[] arr = new int[n];
     search(arr, n, k, result);
  }

  public static void main(String[] args) {
     long start = System.currentTimeMillis();
     permute(10, 8);
     long end = System.currentTimeMillis();
     System.out.println((end - start) / 1000.0);
  }

}


