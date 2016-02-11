import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Created by keks on 2/11/16.
 */
public class Problem22 {

    private static final String FILEPATH = "/home/keks/git/project-euler/p22/names.txt";


    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        int result = 0;

        List<String> lines = readInput(FILEPATH);  /* Unfortunately, all names are in one long line */
        String[] names = lines.get(0).split(",");
        names = removeDoubleQuote(names);

        //Arrays.sort(names);
        //Sorting here (implement own quick- or mergesort or smth
        MergeSort.mergeSort(names);

        for (int i = 0; i < names.length; i++) {
            result += (i + 1) * sum(names[i]);
        }

        System.out.printf("Total sum: %d\n", result);

        System.out.printf("Total runtime: %d ms", System.currentTimeMillis() - start);
        return;
    }

    public static String[] removeDoubleQuote(String[] names) {
        for (int i = 0; i < names.length; i++) {
            names[i] = names[i].replaceAll("\"", "");
        }
        return names;
    }

    public static List<String> readInput(String filepath) {
        List<String> lines = new ArrayList<>();

        try (BufferedReader br = Files.newBufferedReader(Paths.get(filepath))) {
            //String line = null;
            //while (br.readLine() != null)
            lines = br.lines().collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lines;
    }

    public static int sum(String name) {
        int sum = 0;
        for (int i = 0; i < name.length(); i++) {
            sum += Character.getNumericValue(name.charAt(i)) - 9;  /* A-Z have numeric values of 10-35 */
        }
        return sum;
    }
}

class MergeSort {

    private static Comparable[] aux;

    public static void mergeSort(Comparable[] a) {
        aux = new Comparable[a.length];  /* Initialize auxiliary array once */
        mSort(a, 0, a.length - 1);
    }

    public static void mSort(Comparable[] a, int lo, int hi) {
        /*
        1) If array a has length 0 or 1 it is already sorted
        2) Otherwise, split array in half and sort each recursively
        3) Merge sorted halves back together into sorted array
         */
        if (lo >= hi) {
            return;
        }
        int mid = lo + (hi - lo) / 2;
        mSort(a, lo, mid);
        mSort(a, mid + 1, hi);
        merge(a, lo, mid, hi);
    }

    public static void merge(Comparable[] a, int lo, int mid, int hi) {
        /*
        Merge sorted a[lo..mid] and a[mid+1..hi] s.t. afterwards a[lo..hi] is sorted
         */
        int i = lo;
        int j = mid + 1;

        for (int k = lo; k <= hi; k++) {  /* Copy values of a[lo..hi] to auxiliary array */
            aux[k] = a[k];
        }

        for (int k = lo; k <= hi; k++) {  /* Merge back to sorted a[lo..hi] */
            if (j == hi + 1 || i <= mid && (aux[i].compareTo(aux[j]) < 0)) {
                a[k] = aux[i];
                i++;
            } else {
                a[k] = aux[j];
                j++;
            }
        }
    }
}
