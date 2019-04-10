import csv

class CSVReader:
    def __init__(self):
        pass
        
    @staticmethod
    def readCSV(filepath):
        return [rows.strip().split(',') for rows in open(filepath)]
    
    
class getIngredient:
    
    def __init__(self):
        self.ingredientsArray = CSVReader.readCSV('ingredients.csv')
        
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
    def __init__(self):
        self.getIng = getIngredient()
        self.pantryList = []
    
    def addIngredient(self, ID, amount):
        ingredient = self.getIng.findEntry(ID)
        if ingredient != None:
            flag = False
            for i in self.pantryList:
                if ingredient == self.pantryList[i][0]:
                    flag = True
            if not flag:
                newEntry = [ingredient,0]
                self.pantryList.append(newEntry)
            self.increaseAmount(ID, amount);
            return
        return
    
    def increaseAmount(self, ID, amount):
        ingredient = self.getIng.findEntry(ID)
        for i in self.pantryList:
            if ingredient == self.pantryList[i][0]:
                newAmount = int(self.pantryList[i][0] + amount)
                self.pantryList[i] = [self.pantryList[i][0], newAmount]
                return
        return
    
    def filter(self, category):
        filterArray = []
        for e in range(2,18):
            if category == self.getIng.ingredientsArray[0][e]:
                for i in self.pantryList:
                    g = int(self.pantryList[i][0][e])
                    if g == 1:
                        filterArray.append(self.pantryList[i])
        return filterArray
