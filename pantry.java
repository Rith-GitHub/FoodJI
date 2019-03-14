import java.util.*;

public class pantry {
    private ArrayList<Object[][]> pantry = new ArrayList<Object[][]>();
    
    public pantry() {
        getIngredient getIngredient;
    }
    
    public void addIngredient(String ID) {
        String[] ingredient = getIngredient.findEntry(ID);
        if (ingredient != null) {
            boolean flag = false;
            for (int i = 0; i < pantry.size(); i++) {
                if (ingredient == pantry.get(i)[0]) {
                    flag = true;
                }
            }
            if (!flag) {
                Integer[] a = new Integer[] {0};
                Object[][] newEntry = new Object[][] {ingredient, a};
                pantry.add(newEntry);
            }
            increaseAmount(ID);
            return;
        }
        return;
    }
    
    public void increaseAmount(String ID) {
        String[] ingredient = getIngredient.findEntry(ID);
        Scanner sc = new Scanner(System.in);
        int amount;
        try {amount = sc.nextInt();} //**Change amount input method later
        catch(Exception e) {return;}
        
        for (int i = 0; i < pantry.size(); i++) {
            if (ingredient == pantry.get(i)[0]) {
                int a = (int) pantry.get(i)[1][0];
                Integer[] newAmount = new Integer[] {a + amount};
                Object[][] newObj = new Object[][] {pantry.get(i)[0], newAmount};
                pantry.set(i, newObj);
                return;
            }
        }
        return;
    }
    
    /*public ArrayList<Object> filter(String[] category) {
        ArrayList<Object[]> filterArray = new ArrayList<Object[]>();
        for (int c = 0; c < category.length; c++) {
            for (int e = 2; e < 18; e++) {
                if (category[c] == pantry.get(0)[0][e]) {
                    for (int i = 1; i < pantry.length(); i++) {
                        if (pantry.get(i)[0][e] == 1) {
                            filterArray.add(pantry.get(i));
                        }
                    }
                }
            }
        }
        return filterArray;
    }*/
    public ArrayList<Object[]> filter(String category) {
        ArrayList<Object[]> filterArray = new ArrayList<Object[]>();
        for (int e = 2; e < 18; e++) {
            if (category == getIngredient.ingredientsArray.get(0)[e]) {
                for (int i = 1; i < pantry.size(); i++) {
                    int g = (int) pantry.get(i)[0][e];
                    if (g == 1) {
                        filterArray.add(pantry.get(i));
                    }
                }
            }
        }
        return filterArray;
    }

}
