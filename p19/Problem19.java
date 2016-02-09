import java.util.Calendar;

/**
 * Created by keks on 2/9/16.
 */
public class Problem19 {
    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        Calendar c = Calendar.getInstance();
        int sundays = 0;

        for (int year = 1901; year <= 2000; year++) {
            for (int month = 0; month <= 11; month++) {
                c.set(year, month, 1); // months are zero based

                if (c.get(Calendar.DAY_OF_WEEK) == 1) {
                    sundays++;
                }
            }
        }
        System.out.printf("%d sundays fell on the first of the month during the 20th century", sundays);

        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
    }
}
