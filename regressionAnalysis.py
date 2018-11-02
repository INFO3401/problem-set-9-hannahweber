# Monday Problems - worked with Taylor, Marissa, Jacob, Jack
import csv
import pandas as pd

# Part A
class AnalysisData:

    def __init__(self):
        self.dataset = []
        self.variables = []

    def parseFile(self, filename):
        self.dataset = pd.read_csv(filename)
        for column in self.dataset.columns.values:
            if column != "competitorname":
                self.variables.append(column)
        

# Part B

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
class LinearAnalysis:
    
    def __init__(self, targetY_input):
        self.bestX = ""
        self.targetY = targetY_input
        self.fit = ""
        
    def runSimpleAnalysis(self, data):
        regr = LinearRegression()
        regr.fit(<candy>, <sugar>)
        regr.predict(<candy>)
        r2_score(<sugar>, <predicted values>)

# Part C
class LogisticAnalysis:
    
    def __init__(self, targetY_input):
        self.bestX = ""
        self.targetY = targetY_input
        self.fit = ""
        
# Problem 1
data = AnalysisData()
data.parseFile("candy-data.csv")

#Problem 2 - shown in Part B and C

# Wednesday Problems - worked with Taylor, Marissa, Jack
# Problem 3

