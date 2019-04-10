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
            
