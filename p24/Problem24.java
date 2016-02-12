import java.util.ArrayList;
import java.util.List;

/**
 * Created by keks on 2/12/16.
 */
public class Problem24 {

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        int limit = 1000000;
        int[] numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        System.out.printf("The millionth lexicographic permutation of numbers 0-9 is: %s\n",
                findPermutation(limit, numbers));

        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
        return;
    }

    public static String findPermutation(int whichPermutation, int[] numbers) {
        String permutation = "";
        int N = numbers.length;
        int remainingPermutations = whichPermutation - 1;  /* We want to find the one after */

        /* Copy numbers such that we can remove them easily */
        List<Integer> numberList = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            numberList.add(numbers[i]);
        }

        /* n items can be permutated in n! ways. Thus, we can deduce which
         * number at a specific position covers the intended range.
         * E.g.: 9! = 362880. Thus, 362880 permutations are upfront in the
         * lexicographic ordering, starting with 0. The next 362880 permutations
         * start with 1. Then, the permutations starting with 2 cover the range
         * between 725760 and 1088640 -> the wanted millionth permutation starts
         * with 2... */
        for (int i = 1; i < N; i++) {
            int currentFact = factorial(N - i);
            int indexOfNumber = remainingPermutations / currentFact;  /* How many ranges of (N-i)! fit */
            remainingPermutations = remainingPermutations % currentFact; /* What's the remainder */
            permutation += numberList.get(indexOfNumber).toString();
            numberList.remove(indexOfNumber);
            if (remainingPermutations == 0) {
                break;
            }

        }

        for (int i = 0; i < numberList.size(); i++) {
            permutation += numberList.get(i).toString();
        }

        return permutation;
    }

    public static int factorial(int n) {
        /* Probably a bad way to compute the factorial,
         * but we only need small ones here */
        int factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        return factorial;
    }
}
