import java.util.*;

public class getIngredient {
    public static ArrayList<String[]> ingredientsArray = new ArrayList<String[]>();
    
    public static void getIngredient(){
        //CSVReader CSVReader;
        ingredientsArray = CSVReader.readCSV("ingredients.csv");
    }
    
    public static String[] findEntry (String inputID) {
        int id;
        try {
            id = Integer.parseInt(inputID);
        }
        catch(Exception e) {
            return null;
        }
        for (int i = 0; i < ingredientsArray.size(); i++) {
            String [] entryList = ingredientsArray.get(i);
            try {
                int entryID = Integer.parseInt(entryList[0]);
                if (id == entryID) {
                    return entryList;
                }
            }
	    catch (Exception e) {;}
        }
        return null;
    }
}
