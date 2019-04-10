import csv

class CSVReader:
    def __init__(self):
        pass
        
    @staticmethod
    def readCSV(filepath):
        return [rows.strip().split(',') for rows in open(filepath)]
