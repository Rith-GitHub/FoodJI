from __future__ import print_function
import sys
from abc import ABC, abstractmethod
import csv
import math

'''Class that reads CSV files'''
class fileReader:
    def __init__(self):
        pass

    @staticmethod
    def readCSV(filepath):
        '''Reads CSV and converts into 2d Array

        :param filepath: filepath from directory of this file to the csv's
                         directory
        :type filepath: str
        :returns: 2d array
        '''
        a = []
        with open(filepath) as file:
            for row in csv.reader(file, quotechar='"', delimiter=',', \
                                  quoting=csv.QUOTE_ALL, skipinitialspace=True):
                a.append(row)
        return a

'''Abstract class defining methods for database entries'''
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

''''''
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

'''Formats individual entry from ingredients CSV'''
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

'''Extends from ingredient class with additional instance variable to count how
much of the ingredient of is possession of the user'''
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

'''Formats ingredients database and has ability to search through it for
specific ingredients'''
class getIngredient:

    def __init__(self):
        '''Takes list of entries from ingredients database ingredients.csv and
        converts them into objects of class type ingredient
        '''
        self.ingredientsArray = fileReader.readCSV('ingredients.csv')
        for e in range(0, len(self.ingredientsArray)):
            self.ingredientsArray[e] = ingredient(self.ingredientsArray[e])

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
                return entry
        return

'''Formats individual entry from recipe csv'''
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
        #print(' '*5+str(ingSection))
        self.ingredients = self._formatCategory(ingSection, 'ingredients', \
                                                type = 'ingredients')
        insSection = []
        for row in range(insIndex, len(inputArray2d)):
            insSection.append(inputArray2d[row][2:])
        #print('b')
        #print(' '*5+str(insSection))
        self.instructions = self._formatCategory(insSection, 'instructions', \
                                                 type = 'instructions')
        if type(self.id) is int:
            imagesrc = 'recipe images/'
            if self.id > 0:
                imagesrc += '0' * (3 - int(math.log10(self.id)+1)) + \
                            str(self.id) + '/' + inputArray2d[0][9]
            else:
                imagesrc += '000/' + inputArray2d[0][9]
            self.image = imagesrc
        else:
            self.image = None

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
                    for row in range(section[1], list[indexOfNext][1]):
                        #creates subArray
                        subSection.append(array[row][1:])
                else:
                    for row in range(section[1], len(array)):
                        subSection.append(array[row][1:])
                #print(subSection)
                if len(subSection) == 1 and type == 'ingredients':
                    subSection.append(['']*len(subSection[0]))
                #print(' '*7+str(subSection))
                x, y = self._formatCategory(subSection, newCategory, type)
                returnDict[x] = y
            return returnDict
        elif len(array) == 2:
            if type == 'ingredients' and category != 'ingredients':
                list = [] #will be returned
                for e in range(0,len(array[0])):
                    if (array[0][e], array[1][e]) != ('',''):
                        newIngredient = getIngredient().findEntry(array[0][e])
                        list.append((newIngredient, array[1][e]))
                #print(' '*9+str(list))
                return category, list
            elif type == 'ingredients' and category == 'ingredients':
                dict = {}
                #print(' '*7+str([array[0][1:], array[1][1:]]))
                x,y = self._formatCategory([array[0][1:], array[1][1:]], array[0][0], type)
                dict[x] = y
                return dict
            elif type == 'instructions':
                list = []
                instructList = {}
                for e in array:
                    for b in range(1,len(e)):
                        if e[b] != '':
                            list.append(e[b])
                    #print([list])
                    #print(' '*7+str([e]))
                    x, y = self._formatCategory([e], e[0], type)
                    instructList[x] = y
                    list = []
                return instructList
        else: #length of array is one
            if type == 'instructions' and category != 'instructions':
                list = []
                for e in range(0, len(array[0])):
                    if array[0][e] != '':
                        list.append(array[0][e])
                #print(' '*9+str(list))
                return category, list
            elif type == 'instructions' and category == 'instructions':
                dict = {}
                #print(' '*7+str(array[0][1:]))
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

    def getTotalT(self, calcHours = False):
        '''Returns total time to complete recipe

        :rtype: int
        '''
        totalTime = self.prepTime + self.cookTime
        if calcHours and totalTime >= 60:
            minutes = totalTime % 60
            hours = (totalTime - minutes) / 60
            return hours, minutes
        elif calcHours:
            return 0, totalTime
        else:
            return totalTime

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

    def getIng(self, asString = False):
        '''Returns ingredients for recipe

        :return: dictionary of ingredients
        :rtype: dictionary
        '''
        returnDict = {}
        if asString:
            for category in self.ingredients:
                list = []
                for ingredient in self.ingredients[category]:
                    list.append((ingredient[0].getName(), ingredient[1]))
                returnDict[category] = list
                list = []
            return returnDict
        else:
            return self.ingredients

    def getIns(self):
        '''Returns instructions from recipe

        :rtype: dictionary
        '''
        return self.instructions

    def getImagesrc(self):
        '''

        :returns: filepath to recipe image
        :rtype: string
        '''
        return self.image

'''Formats recipe database and has ability to find specific recipes in it'''
class getRecipes:

    def __init__(self):
        recipeArray = fileReader.readCSV('recipes.csv')
        self.recipeArray = []
        entry = []
        for num in range(0, len(recipeArray)):
            if recipeArray[num][0] != '' and len(entry) != 0:
                entryFormatted = recipe(entry)
                self.recipeArray.append(entryFormatted)
                entry = []
            entry.append(recipeArray[num])
        else:
            entryFormatted = recipe(entry)
            self.recipeArray.append(entryFormatted)
        if self.recipeArray[0].getID() == 'Index':
            del self.recipeArray[0]

    def findEntry(self, input = None):
        id = None
        #name = None
        if input == None:
            return
        elif type(input) is int:
            id = int(input)
        #elif type(input) is str:
        #    name = str(input)
        for entryNum in range(1, len(self.recipeArray)):
            entry = self.recipeArray[entryNum]
            entryID = entry.getID()
        #    entryName = entry.getName()
            if id == entryID: #or name == entryName:
                return entry
        return

    def getRecipes(self, asString = False):
        if asString:
            returnList = []
            for recipe in self.recipeArray:
                returnList.append(recipe.getName())
            return returnList
        return self.recipeArray

'''Environment for user inventory and recipe recommendations
'''
class environment:
    def __init__(self):
        self.getIng = getIngredient()
        self.pantryList = []
        self.recipes = getRecipes()
        self.recommendations = []
        #self.organize()

    def addIngredient(self, id, amount):
        ingredient = self.getIng.findEntry(id)
        if ingredient != None and self.findIngredient(id) == None:
            self.pantryList.append(pantryEntry(ingredient, 0))
        self.increaseAmount(id, amount)
        return

    def increaseAmount(self, ID, amount):
        ingredient = self.findIngredient(ID)
        if ingredient != None:
            ingredient.changeAmount(amount)
            if ingredient.getAmount() <= 0:
                self.pantryList.remove(ingredient)
        return

    def findIngredient(self, input = None):
        id = None
        name = None
        if input == None:
            return
        elif type(input) is int:
            id = int(input)
        elif type(input) is str:
            name = str(input)
        for entry in self.pantryList:
            entryID = entry.getID()
            entryName = entry.getName()
            if id == entryID or name == entryName:
                return entry
        return

    def getPercent(self, input):
        if isinstance(input, recipe): #if input is a recipe object
            ingredients = input
        else: #otherwise (assuming input is an id instead)
            ingredients = self.recipes.findEntry(input)
        totalRequired = 0 #amount of ingredients needed
        totalPossessed = 0 #amount of ingredients in possession
        ingredientsReq = []
        for category in ingredients.getIng():
            for ingredient in ingredients.getIng()[category]:
                for e in ingredientsReq:
                    if e[0] == ingredient[0]:
                        e[1] += float(ingredient[1])
                        break
                else:
                    if ingredient[1] != '':
                        ingredientsReq.append([ingredient[0], float(ingredient[1])])
                    else:
                        ingredientsReq.append([ingredient[0], 0])
        for e in ingredientsReq:
            ingredientPos = self.findIngredient(e[0].getID())
            totalRequired += e[1]
            if isinstance(ingredientPos, pantryEntry) and \
                          ingredientPos.getAmount() >= e[1]:
                totalPossessed += e[1]
            elif isinstance(ingredientPos, pantryEntry) and \
                            ingredientPos.getAmount() > 0:
                totalPossessed += ingredientPos.getAmount()
        return totalPossessed*100//totalRequired

    def quicksort(self,low=None,high=None,start=True,sortRecipes=False):
        arr = self.recipes.recipeArray
        if start:
            low = 0
            high = len(arr)-1
        def partition(arr, low, high):
            i = (low-1)
            if sortRecipes:
                pivot = self.getPercent(arr[high])
            else:
                pivot = arr[high]
            for j in range(low, high):
                if sortRecipes:
                    check = self.getPercent(arr[j])
                else:
                    check = arr[j]
                if check >= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i+1)
        if low < high:
            pi = partition(arr, low, high)
            self.quicksort(low=low,high =pi-1,start=False, \
                           sortRecipes=sortRecipes)
            self.quicksort(low=pi+1,high=high,start=False, \
                           sortRecipes=sortRecipes)

    def filter(self, category):
        filterArray = []
        ingArray = self.getIng.ingredientsArray
        for catNum in range(0,len(ingArray[0].getCategory())):
            if category == ingArray[0].getCategory()[catNum]:
                for i in self.pantryList:
                    if int(self.pantryList[i][0][catNum]) == 1:
                        filterArray.append(self.pantryList[i])
        return filterArray

    def getPantryList(self, asString = False):
        returnList = []
        if asString:
            for index in range(0,len(self.pantryList)):
                returnList.append(self.pantryList[index].getName() + '(' + \
                                  str(self.pantryList[index].getAmount())+')')
            return returnList
        return self.pantryList

DEMO = True;
if DEMO:
    print(sys.version)       #Print Python Version
    pantry = environment()   #Initialize environment
    recipes = pantry.recipes #Save instance variable as shorter name
                             #   (It's just easier to understand this way)

    pantry.addIngredient('Mitsuba', 10)    #Add 10 'Mitsuba' to inventory
    pantry.addIngredient('Green Onion', 4) #Add 4 'Green Onion'
    pantry.addIngredient(416, 2)           #Add 2 of ingredient #416
                                           #   (vanilla yogurt)
    print(pantry.getPantryList(True))      #List inventory (parameter set to
                                           #   True makes it return array as
                                           #   string)

    meal = recipes.findEntry(1)     #Save recipe #1 (Beef Udon) as 'meal'
    print('Try ' + meal.getName())  #Print name of 'meal'
    print(meal.getIng(True))        #Print ingredients required for recipe
                                    #   Again, parameter True makes it string
    print(pantry.getPercent(meal))  #Print percent of required ingredients in
                                    #   inventory

    print(recipes.getRecipes(True))      #Print original order of recipes
    pantry.quicksort(sortRecipes = True) #Reorders recipes based on percent of
                                         #   completion
    print(recipes.getRecipes(True))      #Prints new order of recipes
