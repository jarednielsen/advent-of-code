import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Represent it with a boolean array of 0 and 1.
 * Wrap around by doing mod on the horizontal axis.
*/

public class dec03 {
    public static void main(String[] args) {
        ArrayList<String> lines = new ArrayList<String>();
        try {
            File file = new File("dec03_input.txt");
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                String data = scanner.nextLine();
                lines.add(data);
                // System.out.println(data);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
            e.printStackTrace();
        }
        System.out.println(lines);
        System.out.println(lines.get(0).length() + ", " + lines.size());
        int width = lines.get(0).length();
        int height = lines.size();

        // Index the array as (x,y)
        boolean[][] arr = new boolean[width][height];
        for(int y = 0; y < height; y++) {
            String line = lines.get(y);
            System.out.println(line);
            for(int x = 0; x < width; x++) {
                arr[x][y] = line.charAt(x) == '#';
            }
        }

        for(boolean[] line : arr) {
            System.out.println(Arrays.toString(line));
        }

        int trees = 0;
        int x_pos = 0;
        int y_pos = 0;
        int i = 0;
        while(y_pos < height) {
            if(arr[x_pos][y_pos]) {
                trees++;
            }
            i += 1;
            x_pos = (1 * i) % width;
            y_pos = 2 * i;
        }
        System.out.println("Trees: " + trees);
    }
}