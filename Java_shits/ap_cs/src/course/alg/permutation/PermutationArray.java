package course.alg.permutation;

import java.util.ArrayList;

public class PermutationArray {
  static void search(int[] arr, int n, ArrayList<Integer> result) {
     if (result.size() == n) {
        // System.out.println(result);
     } else {
        for (int i = 0; i < n; i++) {
           if (arr[i] == 1)
              continue;
           // choose
           arr[i] = 1;
           // System.out.println(Arrays.toString(arr));
           result.add(i);
           // permute
           search(arr, n, result);
           // unchoose
           arr[i] = 0;
           // System.out.println(Arrays.toString(arr));
           result.remove(result.size() - 1);
        }
     }
  }

  static void permute(int n) {
     ArrayList<Integer> result = new ArrayList<>();
     int[] arr = new int[n];
     search(arr, n, result);
  }

  public static void main(String[] args) {
     long start = System.currentTimeMillis();
     permute(10);
     long end = System.currentTimeMillis();
     System.out.println((end - start) / 1000.0);
  }

}


