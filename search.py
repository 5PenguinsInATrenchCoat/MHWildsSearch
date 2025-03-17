import csv
from constants import *

class Search():
    def __init__(self, skill1 = None, level1 = None, skill2 = None, level2 = None, skill3 = None, level3 = None, skill4 = None, level4 = None, skill5 = None, level5 = None):
        self.skill1 = skill1
        self.level1 = level1

        self.skill2 = skill2
        self.level2 = level2

        self.skill3 = skill3
        self.level3 = level3

        self.skill4 = skill4
        self.level4 = level4

        self.skill5 = skill5
        self.level5 = level5

    #Assigns skills 1-5, along with the desired levels. These are what we're looking to return on each armor set in the output.



 