from __future__ import print_function
from abc import ABC, abstractmethod
import csv

class fileReader:
    def __init__(self):
        pass

    @staticmethod
    def readCSV(filepath):
        '''Reads CSV and converts into 2d Array

        :param filepath: filepath from directory of this file to the csv's directory
        :type filepath: str
        :returns: 2d array
        '''
        a = []
        with open(filepath) as file:
            for row in csv.reader(file, quotechar='"', delimiter=',', \
                                  quoting=csv.QUOTE_ALL, skipinitialspace=True):
                a.append(row)
        '''if DEBUG:
            print('fileReader readCSV')
            for row in range(0,5):
                print(a[row])
            print('\n')'''
        return a

class databaseEntry(ABC):

    def __init__(self, input):
        self.input = input
        super().__init__()

    @abstractmethod
    def getID(self):
        pass

    @abstractmethod
    def getName(self):
        pass

class userEntry(databaseEntry, ABC):

    def __init__(self, input):
        self.input = input
        super().__init__()

    @abstractmethod
    def getAmount(self):
        pass

    @abstractmethod
    def changeAmount(self):
        pass

class ingredient(databaseEntry):
    def __init__(self, inputArray):
        '''Formats array inputted from csv file of ingredients

        :param inputArray: entry from ingredients database.
        :type inputArray: Formatted array
        '''
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
        '''Returns ID of instance

        :rtype: int
        '''
        return self.id

    def getName(self):
        '''Returns name of instance

        :rtype: str
        '''
        return self.name

    def getCategory(self):
        '''Returns categories of instance

        :returns: formatted array
        '''
        return self.category

class pantryEntry(ingredient, userEntry):
    def __init__(self, inputIngredient, amount):
        '''Extends from ingredient class. Adds instance variable to count the
        amount of ingredient that is in possession of the user.

        :param inputIngredient: ingredient in possession of the user
        :type inputIngredient: ingredient
        :param int amount: counter for the amount of ingredient possessed
        '''
        self.id = inputIngredient.getID()
        self.name = inputIngredient.getName()
        self.category = inputIngredient.getCategory()
        try:
            self.amount = int(amount)
        except:
            self.__class__ = ingredient

    def getAmount(self):
        '''Returns amount in possession
        :rtype: int
        '''
        return self.amount

    def changeAmount(self, amount):
        '''Edits counter
        :param int amount: the amount the counter is changed by
        '''
        self.amount += amount

class getIngredient:

    def __init__(self):
        '''Takes list of entries from ingredients database ingredients.csv and
        converts them into objects of class type ingredient
        '''
        self.ingredientsArray = fileReader.readCSV('ingredients.csv')
        for e in range(0, len(self.ingredientsArray)):
            self.ingredientsArray[e] = ingredient(self.ingredientsArray[e])
        '''if DEBUG:
            print('getIngredient init')
            for i in range(1,7):
                a = self.ingredientsArray[i]
                alist = [a.getID(),a.getName(),a.getCategory()]
                print(' '.join(map(str, alist)))
            print('\n')'''

    def findEntry(self, input = None):
        id = None
        name = None
        if input == None:
            return
        elif type(input) is int:
            id = int(input)
        elif type(input) is str:
            name = str(input)
        for entryNum in range(1, len(self.ingredientsArray)):
            entry = self.ingredientsArray[entryNum]
            entryID = entry.getID()
            entryName = entry.getName()
            if id == entryID or name == entryName:
                '''if DEBUG:
                    print('entry '+entry.getName()+' found.\nid: '+str(id)+'\nentryID:'+str(entryID))'''
                return entry
        '''if DEBUG:
            print('entry not found\nid: ' + str(id))'''
        return

class pantry:
    def __init__(self):
        self.getIng = getIngredient()
        self.pantryList = []

    def addIngredient(self, id, amount):
        '''if DEBUG:
            print('pantry addIngredient')'''
        ingredient = self.getIng.findEntry(id)
        if ingredient != None:
            flag = False
            for i in self.pantryList:
                if ingredient.getID() == i.getID():
                    flag = True
            if not flag:
                self.pantryList.append(pantryEntry(ingredient, 0))
            self.increaseAmount(id, amount)
            '''if DEBUG:
                print('id %r found' % id)'''
            return
        '''if DEBUG:
            print('id %r not found' % id)'''
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

    def findEntry(self, input = None):
        self.getIng.findEntry(input)

class recipe(databaseEntry):

    def __init__(self, inputArray2d):
        try:
            self.id = int(inputArray2d[0][0])
        except:
            self.id = inputArray2d[0][0]
        try:
            self.prepTime = int(inputArray2d[0][3])
        except:
            self.prepTime = inputArray2d[0][3]
        try:
            self.cookTime = int(inputArray2d[0][4])
        except:
            self.cookTime = inputArray2d[0][4]
        try:
            self.servings = int(inputArray2d[0][5])
        except:
            self.servings = inputArray2d[0][5]
        self.name = inputArray2d[0][1]
        self.description = inputArray2d[0][2]
        self.author = inputArray2d[0][6]
        self.citing = inputArray2d[0][7]
        self.notes = inputArray2d[0][8]
        self.ingredients = {}
        self.instructions = {}
        ingIndex = None
        intIndex = None
        for row in inputArray2d[1:]:
            if row[1] == 'ingredients':
                ingIndex = inputArray2d.index(row)
            elif row[1] == 'instructions':
                insIndex = inputArray2d.index(row)
        #print(self.name+'\n'+str(ingIndex)+' '+str(insIndex))
        ingSection = []
        for row in range(ingIndex, insIndex):
            ingSection.append(inputArray2d[row][2:])
        #print('a')
        #print(ingSection)
        self.ingredients = self._formatCategory(ingSection, 'ingredients', type = 'ingredients')
        insSection = []
        for row in range(insIndex, len(inputArray2d)):
            insSection.append(inputArray2d[row][2:])
        #print('b')
        #print(insSection)
        self.instructions = self._formatCategory(insSection, 'instructions', type = 'instructions')

    def _formatCategory(self, array, category, type):
        list = [] # list for bounds of each subsection
        if len(array) > 2:
            for row in array:
                if row[0] != '':
                    list.append([row[0], array.index(row)])
            returnDict = {}
            for section in list:
                newCategory = section[0]
                subSection = []
                if list.index(section)+1 != len(list):
                    indexOfNext = list.index(section)+1
                    for row in range(section[1], list[indexOfNext][1]): #creates subArray
                        subSection.append(array[row][1:])
                else:
                    for row in range(section[1], len(array)):
                        subSection.append(array[row][1:])
                #print(subSection)
                x, y = self._formatCategory(subSection, newCategory, type)
                returnDict[x] = y
            return returnDict
        elif len(array) == 2:
            if type == 'ingredients':
                list = [] #will be returned
                for e in range(1,len(array[0])):
                    if (array[0][e], array[1][e]) != ('',''):
                        list.append((array[0][e], array[1][e]))
                #print(list)
                return category, list
            elif type == 'instructions':
                list = []
                instructList = {}
                for e in array:
                    for b in range(1,len(e)):
                        if e[b] != '':
                            list.append(e[b])
                    #print([list])
                    x, y = self._formatCategory([e], e[0], type)
                    instructList[x] = y
                    list = []
                return instructList
        else: #length of array is one
            if type == 'ingredients':
                list = []
                for e in array[0]:
                    if e != '':
                        list.append((e,))
                #print(list)
                return category, list
            elif type == 'instructions' and category != 'instructions':
                list = []
                for e in range(1, len(array[0])):
                    if array[0][e] != '':
                        list.append(array[0][e])
                #print(category)
                #print(list)
                return category, list
            elif type == 'instructions' and category == 'instructions':
                dict = {}
                #print(array)
                x,y = self._formatCategory([array[0][1:]], array[0][0], type)
                dict[x] = y
                return dict

    def getID(self):
        '''Returns ID of instance

        :rtype: int
        '''
        return self.id

    def getName(self):
        '''Returns name of instance

        :rtype: str
        '''
        return self.name

    def getDesc(self):
        '''Returns description of recipe

        :rtype: str
        '''
        return self.description

    def getPrepT(self):
        '''Returns prep time

        :rtype: int
        '''
        return self.prepTime

    def getCookT(self):
        '''Returns cook time

        :rtype: int
        '''
        return self.cookTime

    def getServing(self):
        '''Returns number of servings

        :rtype: int
        '''
        return self.servings

    def getAuthor(self):
        '''Returns name of author

        :rtype: str
        '''
        return self.author

    def getCite(self):
        '''Returns source of recipe

        :rtype: str
        '''
        return self.citing

    def getNotes(self):
        '''Returns recipe notes

        :rtype: str
        '''
        return self.notes

    def getIng(self):
        '''Returns ingredients for recipe

        :return: dictionary of ingredients
        :rtype: dictionary
        '''
        return self.ingredients

    def getIns(self):
        '''Returns instructions from recipe

        :rtype: dictionary
        '''
        return self.instructions

    def debug(self):
        list = [self.name, self.ingredients, self.instructions]
        print('\n'.join(map(str, list)))

class getRecipes:

    def __init__(self):
        recipeArray = fileReader.readCSV('recipes.csv')
        self.recipeArray = []
        entry = []
        for num in range(0, len(recipeArray)):
            if recipeArray[num][0] != '' and len(entry) != 0:
                entryFormatted = recipe(entry)
                '''if DEBUG:
                    print(entryFormatted.name)'''
                self.recipeArray.append(entryFormatted)
                entry = []
            entry.append(recipeArray[num])
        entryFormatted = recipe(entry)
        '''if DEBUG:
            print(entryFormatted.name)'''
        self.recipeArray.append(entryFormatted)
        '''if DEBUG:
            print('getRecipes init')
            a = self.recipeArray[3]
            print(a.debug())
            print('\n')'''

    def findEntry(self, input = None):
        id = None
        name = None
        if input == None:
            return
        elif type(input) is int:
            id = int(input)
        elif type(input) is str:
            name = str(input)
        for entryNum in range(1, len(self.recipeArray)):
            entry = self.recipeArray[entryNum]
            entryID = entry.getID()
            entryName = entry.getName()
            if id == entryID or name == entryName:
                '''if DEBUG:
                    print('entry '+entry.getName()+' found.\nid: '+str(id)+'\nentryID:'+str(entryID))'''
                return entry
        '''if DEBUG:
            print('entry not found\nid: ' + str(id))'''
        return

DEBUG = True;
if DEBUG:
    pantry = pantry()
    recipe = getRecipes()

    pantry.addIngredient(5, 10)
    pantry.addIngredient(250, 4)
    pantry.increaseAmount(250, 6)
    for food in pantry.getPantryList():
        print(', '.join(map(str,[food.getName(),food.getAmount()])))

    meal = recipe.findEntry(1)
    dessert = recipe.findEntry('Yogurt & Fruit Parfaits')
    print('We will have ' + ' and '.join(map(str,[meal.getName(),dessert.getName()])))
    print(meal.getIng())
