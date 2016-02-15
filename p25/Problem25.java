import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by keks on 2/15/16.
 */
public class Problem25 {
    static Map<Integer, BigInteger> memo;

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        BigInteger ten = BigInteger.valueOf(10);
        BigInteger limit = ten.pow(999);  /* value with 1000 digits */

        memo = new HashMap<>();
        memo.put(1, BigInteger.valueOf(1));
        memo.put(2, BigInteger.valueOf(1));

        int n = 1;
        while (fib(n).compareTo(limit) == -1)  {
            n++;
        }
        System.out.println(n);

        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
    }

    public static BigInteger fib(int n) {
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        BigInteger fib = fib(n - 1).add(fib(n - 2));
        memo.put(n, fib);
        return fib;
    }
}
