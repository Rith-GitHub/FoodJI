public class pantry {
    private Arraylist<Object[]> pantry = new Arraylist<Object[]>();
    
    public pantry() {
        getIngredient;
    }
    
    public void addIngredient(String ID) {
        String[] ingredient = getIngredient.findEntry(ID);
        if (ingredient != null) {
            boolean flag = false;
            for (i = 0; i < pantry.length(); i++) {
                if (ingredient == pantry.get(i)[0]) {
                    flag = true;
                }
            }
            if (not flag) {
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
        
        for (i = 0; i < pantry.length(); i++) {
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
    
    public Arraylist<Object> filter(String[] category) {
        Arraylist<Object[]> filterArray = new Arraylist<Object[]>;
        for (c = 0; c < category.length(); c++) {
            for (e = 2; e < 18; e++) {
                if (c == pantry.get(0)[0][e]) {
                    for (i = 1; i < pantry.length(); i++) {
                        if (pantry.get(i)[0][e] == 1) {
                            filterArray.add(pantry.get(i));
                        }
                    }
                }
            }
        }
        return filterArray;
    }
    public Arraylist<Object> filter(String category) {
        Arraylist<Object[]> filterArray = new Arraylist<Object[]>;
        for (e = 2; e < 18; e++) {
            if (category == pantry.get(0)[0][e]) {
                for (i = 1; i < pantry.length(); i++) {
                    if (pantry.get(i)[0][e] == 1) {
                        filterArray.add(pantry.get(i));
                    }
                }
            }
        }
        return filterArray;
    }

}
