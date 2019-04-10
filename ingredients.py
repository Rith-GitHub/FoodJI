import csv

class CSVReader:
    def __init__(self):
        pass
        
    @staticmethod
    def readCSV(filepath):
        return [rows.strip().split(',') for rows in open(filepath)]

class getIngredient:
    ingredientsArray = []
    
    def __init__(self):
        ingredientsArray = readCSV('ingredients.csv')
        
    def findEntry(self, inputID):
        try:
            id = int(inputID)
        except:
            return
        for entryList in ingredientsArray:
            entryID = int(entryList[0])
            try:
                if id == entryID:
                    return entryList
            except:
                pass
        return

class pantry:
    pantryList = [][]
    
    def __init__(self):
        getIng = getIngredient()
    
    def addIngredient(self, ID, amount):
        ingredient = getIng.findEntry(ID)
        if ingredient != None:
            flag = False
            for i in pantryList:
                if ingredient == pantryList[1][0]:
                    flag = True
            if not flag:
                newEntry = [ingredient,0]
                pantry.append(newEntry)
            increaseAmount(ID, amount);
            return
        return
    
    def increaseAmount(self, ID, amount):
        ingredient = getIng.findEntry(ID)
        for i in pantryList:
            if ingredient == pantryList[1][0]:
                newAmount = int(pantryList[1][0] + amount
                pantryList[i] = [pantryList[1][0], newAmount]
                return
        return
                                
    def filter(self, category):
        filterArray = [][]
        
