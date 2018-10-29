Monday Problems

import csv

class AnalysisData(object):

# initialize any attributes and hand prepocessing
def __init__(self, type):
    self.type = type
    self.dataset = []

# define a function
def parseFile(self, filename):
    with open("candy-data.csv") as csv_file:
        if (self.type == “csv”):
            reader = csv.reader(open(filename))
            for row in reader:
                self.data.append(row)
        else:
            self.data = open(filename).read()