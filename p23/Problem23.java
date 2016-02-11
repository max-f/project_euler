import java.util.*;

/**
 * Created by keks on 2/11/16.
 */
public class Problem23 {
    public static void main(String[] args)  {
        long start = System.currentTimeMillis();

        int limit = 28123;
        List<Integer> notRepresentable = new ArrayList<>();

        Set<Integer> abundantNumbers = getAbundantNumbers(limit);
        Set<Integer> representable = getRepresentable(abundantNumbers, limit);

        /* Get all integers which are not representable as sum of
         * two abundant numbers */
        for (int i = 1; i < limit; i++) {
            if (!representable.contains(i)) {
                notRepresentable.add(i);
            }
        }

        System.out.printf("Total sum of integers which are not representable by a sum of two abundant numbers: %d\n",
                sumList(notRepresentable));

        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
        return;
    }

    public static Set<Integer> getRepresentable(Set<Integer> abundantNumbers, int limit) {
        /* Find integers which are representable by the sum of two abundant numbers,
         * up to limit */
        Set<Integer> representable = new HashSet<>();
        representable.add(24);

        for (int i = 25; i < limit; i++) {
            for (int abundant : abundantNumbers) {
                if (abundantNumbers.contains(i - abundant)) {
                    representable.add(i);
                    break;
                }
            }
        }
        return representable;
    }

    public static Set<Integer> getAbundantNumbers(int limit) {
        Set<Integer> abundantNumbers = new HashSet<>();
        abundantNumbers.add(12);

        for (int i = 13; i <= limit; i++) {  /* 12 is the smallest abundant number */
            List<Integer> divisors = getDivisors(i);
            if (i < sumList(divisors)) {
                abundantNumbers.add(i);
            }
        }
        return abundantNumbers;
    }

    public static int sumList(List<Integer> numberList) {
        return numberList.stream().mapToInt(Integer::intValue).sum();
    }

    public static List<Integer> getDivisors(int n) {
        List<Integer> divisors = new ArrayList<>();
        divisors.add(1);
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                if (Math.pow(i, 2) == n) {
                    divisors.add(i);
                } else {
                    divisors.add(i);
                    divisors.add(n / i);
                }
            }
        }
        return divisors;
    }
}
