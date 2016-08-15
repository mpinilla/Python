import matplotlib.pyplot as plt 
import numpy as np
from numpy import genfromtxt
import re
import os
import shutil

class GetTally():
    def __init__(self):
        self.x = []
        self.y = []
        self.e = []

    def extractf8(self, filename, bins, mult):
        lookup = '1tally        8'
        out = []
        with open(filename) as f:
            content = f.readlines()
        for num, line in enumerate(content, 1):
            if lookup in line:
                for i in range(0, bins + 2):
                    out = content[num + 6 + i].split(' ')
                    self.x.append(str(out[4]))
                    self.y.append(str(float(out[7])*mult))
                    self.e.append(str(out[8]))
        return self.x, self.y, self.e

    def extractf18(self, filename, bins, mult):
        lookup = '1tally       18'
        out = []
        with open(filename) as f:
            content = f.readlines()
        for num, line in enumerate(content, 1):
            if lookup in line:
                for i in range(0, bins + 1):
                    out = content[num + 6 + i].split(' ')
                    self.x.append(str(out[4]))
                    self.y.append(str(float(out[7])*mult))
                    self.e.append(str(out[8]))
        return self.x, self.y, self.e

class GetXY():
    def __init__(self):
        self.x = []
        self.y = []

    def getxy(self, filename):
        for i in range (0, len(filename)):
            my_data = genfromtxt(filename, delimiter = ' ')
            x = my_data[:,0]
            y = my_data[:,1]
        if x[0] > 1.0:
            x = x/1000.0
        return x, y

class GetDrift():
    def __init__(self):
        self.x = []
        self.y = []

    def getdrift(self, filename):
        for i in range (0, len(filename)):
            my_data = genfromtxt(filename, delimiter = '\t')
            x = my_data[:,0]
            y = my_data[:,1]
        return x, y
