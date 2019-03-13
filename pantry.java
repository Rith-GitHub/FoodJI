import java.util.*;

public class pantry {
    private ArrayList<Object[]> pantry = new ArrayList<Object[]>();
    
    public pantry() {
        getIngredient getIngredient;
    }
    
    public void addIngredient(String ID) {
        String[] ingredient = getIngredient.findEntry(ID);
        if (ingredient != null) {
            boolean flag = false;
            for (int i = 0; i < pantry.length(); i++) {
                if (ingredient == pantry.get(i)[0]) {
                    flag = true;
                }
            }
            if (!flag) {
                Object[] newEntry = new Object[] {ingredient, 0};
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
        try {int amount = sc.nextInt();}
        catch(Exception e) {return;}
        
        for (int i = 0; i < pantry.length(); i++) {
            if (ingredient == pantry.get(i)[0]) {
                String[] newEntry = pantry.get(i)[0];
                int newAmount = pantry.get(i)[1] + amount;
                Object[] newObj = new Object[] {newEntry, newAmount};
                pantry.set(i, newObj);
                return;
            }
        }
        return;
    }
    
    public ArrayList<Object> filter(String[] category) {
        ArrayList<Object[]> filterArray = new ArrayList<Object[]>();
        for (int c = 0; c < category.length(); c++) {
            for (int e = 2; e < 18; e++) {
                if (c == pantry.get(0)[0][e]) {
                    for (int i = 1; i < pantry.length(); i++) {
                        if (pantry.get(i)[0][e] == 1) {
                            filterArray.add(pantry.get(i));
                        }
                    }
                }
            }
        }
        return filterArray;
    }
    public ArrayList<Object> filter(String category) {
        ArrayList<Object[]> filterArray = new ArrayList<Object[]>();
        for (int e = 2; e < 18; e++) {
            if (category == pantry.get(0)[0][e]) {
                for (int i = 1; i < pantry.length(); i++) {
                    if (pantry.get(i)[0][e] == 1) {
                        filterArray.add(pantry.get(i));
                    }
                }
            }
        }
        return filterArray;
    }

}
