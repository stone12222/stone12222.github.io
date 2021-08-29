package course.alg.permutation;

public class PermutationString {
  static int count = 0;

  static void permute(StringBuilder chosen, StringBuilder available) {
     if (available.length() == 0) {
        System.out.println(chosen);
        count++;
     } else {
        // choose, permute rest, unchoose
        for (int i = 0; i < available.length(); i++) {
           // choose
           String c = available.substring(i, i + 1);
           chosen.append(c);
           available.deleteCharAt(i);
           // permute rest
           permute(chosen, available);
           // unchoose
           available.insert(i, c);
           chosen.deleteCharAt(chosen.length() - 1);
        }
     }
  }

  public static void main(String[] args) {
     StringBuilder available = new StringBuilder("ABCD");
     StringBuilder chosen = new StringBuilder("");
     permute(chosen, available);
     System.out.println(count); // 4!=4*3*2
  }
}


