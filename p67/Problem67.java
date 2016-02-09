import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class Problem67 {
    /*
    Java implementation of the Maximum path sum 1 problem (problem 18) at projecteuler.net.
    As the maximum path from top to bottom is of course equal to the maximum path from bottom to top,
    we can utilize dynamic programming.
     */


    private static final String FILEPATH = "/home/keks/git/project-euler/p67/triangle.txt";

    public static void main(String[] args) throws IOException {
        long start = System.currentTimeMillis();

        int[][] triangle = readInput(FILEPATH);

        // Using dynamic programming from bottom-up.
        for (int i = triangle.length - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].length - 1; j++) {

                int left_child = triangle[i + 1][j];
                int right_child = triangle[i + 1][j + 1];

                triangle[i][j] += getMax(left_child, right_child);

            }
        }
        System.out.printf("Maximum path sum: %d\n", triangle[0][0]);

        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
        return;
    }

    public static int[][] readInput(String filepath) throws IOException {
        String line;
        String[] tokens;
        int[][] triangle = null;
        int lines = 0;
        File file = new File(filepath);

        try(RandomAccessFile raf = new RandomAccessFile(file, "r")) {

            while (raf.readLine() != null) {
                lines++;
            }
            triangle = new int[lines][lines];

            // Reset RandomAccessFile
            raf.seek(0);
            // Fill 2D array
            int i = 0;
            while ((line = raf.readLine()) != null) {
                tokens = line.split(" ");

                for (int j = 0; j < tokens.length; j++) {
                    triangle[i][j] = Integer.parseInt(tokens[j]);
                }
                i++;
            }

        } catch (IOException e) {
            System.out.println("Meh!");
            e.printStackTrace();
        }
        return triangle;
    }

    public static int getMax(int num1, int num2) {
        return (num1 > num2 ? num1 : num2);
    }
}
