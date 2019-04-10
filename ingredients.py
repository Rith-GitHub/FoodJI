import csv

class CSVReader:
    def __init__(self):
        pass
        
    @staticmethod
    def readCSV(filepath):
        return [rows.strip().split(',') for rows in open(filepath)]
    
    
class getIngredient:
    
    def __init__(self):
        self.ingredientsArray = readCSV('ingredients.csv')
        
    def findEntry(self, inputID):
        try:
            id = int(inputID)
        except:
            return
        for entryList in self.ingredientsArray:
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
                newAmount = int(pantryList[1][0] + amount)
                pantryList[i] = [pantryList[1][0], newAmount]
                return
        return
    
    def filter(self, category):
        filterArray = [][]
        for e in range(2,18):
            if category == getIng.ingredientsArray[0][e]:
                for i in pantryList:
                    g = int(pantryList[i][0][e])
                    if g == 1:
                        filterArray.append(pantryList[i])
        return filterArray
    
    
