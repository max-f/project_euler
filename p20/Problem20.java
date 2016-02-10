import java.math.BigInteger;

/**
 * Created by keks on 2/9/16.
 */
public class Problem20 {

    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        int n = 100;

        BigInteger factorial = BigInteger.valueOf(1);
        for (int i = 1; i <= n; i++) {
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }

        int sum = 0;
        BigInteger zero = BigInteger.valueOf(0);
        while (factorial.compareTo(zero) == 1) {
            sum += factorial.mod(BigInteger.valueOf(10)).intValue();
            factorial = factorial.divide(BigInteger.valueOf(10));
        }

        System.out.printf("sum of the numbers in %d! is: %d\n", n, sum);


        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
        return;
    }
}
