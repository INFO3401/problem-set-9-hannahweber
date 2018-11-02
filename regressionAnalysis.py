# Monday Problems - worked with Taylor, Marissa, Jacob, Jack
import csv

# Part A
class AnalysisData:

    def __init__(self):
        self.dataset = []
        self.variables = []

    def parseFile(self, filename):
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self.dataset.append(row)

data = AnalysisData()
data.parseFile("candy-data.csv")

# Part B
class LogisticAnalysis:
    
    def __init__(self):
        self.bestX = ""
        self.targetY = ""
        self.fit = ""

# Part C
class LinearAnalysis:
    
    def __init__(self):
        self.bestX = ""
        self.targetY = ""
        self.fit = ""
        
# Problem 1

import csv

def parseFile(self, filename):
    with open(filename) as csv:
        reader = csv.reader(open(filename))
        for row in reader:
            self.dataset.append(row)

data = AnalysisData()
data.parseFile("candy-data.csv")