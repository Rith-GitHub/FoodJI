from __future__ import print_function

DEBUG = False;

class fileReader:
    def __init__(self):
        pass
        
    @staticmethod
    def readCSV(filepath):
        a = [rows.strip().split(',') for rows in open(filepath)]
        if DEBUG:
            print('fileReader readCSV')
            for row in range(0,5):
                print(a[row])
            print('\n')
        return a
    
class ingredient:
    def __init__(self, inputArray):
        try:
            self.id = int(inputArray[0])
        except:
            self.id = inputArray[0]
        self.name = inputArray[1]
        self.category = []
        for i in inputArray[2:]:
            try:
                self.category.append(int(i))
            except:
                self.category.append(i)
        
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
        
    def getCategory(self):
        return self.category
    
class pantryEntry(ingredient):
    def __init__(self, inputIngredient, counter):
        self.id = inputIngredient.getID()
        self.name = inputIngredient.getName()
        self.category = inputIngredient.getCategory()
        try:
            self.counter = int(counter)
        except:
            self.__class__ = ingredient
    
    def getCounter(self):
        return self.counter
    
    def changeAmount(self, amount):
        self.counter += amount
    
class getIngredient:
    
    def __init__(self):
        self.ingredientsArray = fileReader.readCSV('ingredients.csv')
        for e in range(0, len(self.ingredientsArray)):
            self.ingredientsArray[e] = ingredient(self.ingredientsArray[e])
        if DEBUG:
            print('getIngredient init')
            for i in range(1,7):
                a = self.ingredientsArray[i]
                alist = [a.getID(),a.getName(),a.getCategory()]
                print(' '.join(map(str, alist)))
            print('\n')
    
    def findEntry(self, inputID):
        if DEBUG:
            print('getIngredient findEntry')
        try:
            id = int(inputID)
        except:
            if DEBUG:
                print('input is not an integer')
            return
        for entryNum in range(1, len(self.ingredientsArray)):
            entry = self.ingredientsArray[entryNum]
            entryID = entry.getID()
            if id == entryID:
                if DEBUG:
                    print('entry '+entry.getName()+' found.\nid: '+str(id)+'\nentryID:'+str(entryID))
                return entry
        if DEBUG:
            print('entry not found\nid: ' + id)
        return
    
class pantry:
    def __init__(self):
        self.getIng = getIngredient()
        self.pantryList = []
    
    def addIngredient(self, id, amount):
        if DEBUG:
            print('pantry addIngredient')
        ingredient = self.getIng.findEntry(id)
        if ingredient != None:
            flag = False
            for i in self.pantryList:
                if ingredient.getID() == i.getID():
                    flag = True
            if not flag:
                self.pantryList.append(pantryEntry(ingredient, 0))
            self.increaseAmount(id, amount)
            if DEBUG:
                print('id %r found' % id)
            return
        if DEBUG:
            print('id %r not found' % id)
        return
    
    def increaseAmount(self, ID, amount):
        ingredient = self.getIng.findEntry(ID)
        for i in self.pantryList:
            if ingredient.getID() == i.getID():
                i.changeAmount(amount)
                return
        return
    
    def filter(self, category):
        filterArray = []
        ingArray = self.getIng.ingredientsArray
        for catNum in range(0,len(ingArray[0].getCategory())):
            if category == ingArray[0].getCategory()[catNum]:
                for i in self.pantryList:
                    if int(self.pantryList[i][0][catNum]) == 1:
                        filterArray.append(self.pantryList[i])
        return filterArray
    
    def getPantryList(self):
        return(self.pantryList)

if DEBUG:
    obj = pantry()
    print(obj.getPantryList())
    obj.addIngredient(20, 5)
    obj.addIngredient(8, 2)
    obj.addIngredient(200, 9)
    obj.addIngredient(8, -1)
    for i in obj.getPantryList():
        print(i.getName() +' ' + str(i.getCounter()))