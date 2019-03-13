import java.util.*;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class CSVReader {

    public static ArrayList<String[]> readCSV(String csvFile) {

        BufferedReader br = null;
        String line = "";
        String cvsSplitBy = ",";
        ArrayList<String[]> alist = new ArrayList<String[]>();
        
        try {
            try {br = new BufferedReader(
                new FileReader(csvFile));
            }
            catch(Exception e) {
                return;
            }
            
            while ((line = br.readLine()) != null) {
                // use comma as separator
                String[] temp = line.split(cvsSplitBy);
                alist.add(temp);
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return alist;
        
    }
    
}
