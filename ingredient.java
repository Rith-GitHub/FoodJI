public class getIngredient {
    private Arraylist<String[]> ingredientsArray = new Arraylist<String[]>
    
    public static void getIngredient(){
        ingredientsArray = readCSV("ingredients.csv");
    }
    
    public String[] findEntry (String inputID) {
        int id;
        try {
            id = Integer.parseInt(inputID);
        }
        catch(Exception e) {
            return "Invalid ID";
        }
        for (i = 0; i < ingredientsArray.length(); i++) {
            String [] entryList = ingredientsArray.get(i);
            int entryID = Integer.parseInt(entryList[0]);
            if (id == entryID) {
                return entryList;
            }
        }
        return null;
    }
}
