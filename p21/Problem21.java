import java.util.ArrayList;
import java.util.List;

/**
 * Created by keks on 2/10/16.
 */
public class Problem21 {

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        int limit = 10000 - 1;
        List<Integer> amicableNumbers= new ArrayList<Integer>();

        for (int i = 1; i < limit - 1; i++) {
            if (amicableNumbers.contains(i)) {
                continue;
            }
            int iSum = sumList(getDivisors(i));
            if (iSum > i && iSum <= limit) {
                int jSum = sumList(getDivisors(iSum));
                if (i == jSum) {
                    amicableNumbers.add(i);
                    amicableNumbers.add(iSum);
                }
            }
        }

        System.out.printf("Sum of all amicable numbers below 10000: %d\n", sumList(amicableNumbers));

        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
        return;
    }

    public static int sumList(List<Integer> numberList) {
        return numberList.stream().mapToInt(Integer::intValue).sum();
    }

    public static List<Integer> getDivisors(int n) {
        /*
        Returns all even divisors of an integer including 1, excluding the integer itself.
         */
        List<Integer> divisors = new ArrayList<Integer>();
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
