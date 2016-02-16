import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Created by keks on 2/16/16.
 */
public class Problem26 {
    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        int limit = 1000;

        int maxN = 0;
        int maxCycleLength = -1;

        for (int n = 2; n < limit; n++) {
            int curCycleLength = getCycleLength(n);
            if (curCycleLength > maxCycleLength) {
                maxN = n;
                maxCycleLength = curCycleLength;
            }
        }
        System.out.printf("Longest recurring cycle up to 1/%d: %d with cycle length of %d\n",
                limit, maxN, maxCycleLength);

        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
        return;
    }

    public static int getCycleLength(int n) {
        Set<Integer> remainders = new HashSet<>();
        int remainder = 1 % n;
        remainders.add(remainder);
        while (remainder != 0) {
            remainder *= 10;
            remainder = remainder % n;
            if (remainders.contains(remainder)) {
                break;
            } else {
                remainders.add(remainder);
            }
        }
        return remainders.size();
    }
}
