import csv
from operator import truediv
from sre_constants import MAX_UNTIL
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    class Station():
        def __init__(self, stid, index):
            self.stid = stid
            self.max_list = []
            self.index = index
            
        def maxTemp(self,row):
            if row['STID'] == self.stid:
                if float(row['TMAX']) != -996.00:
                    self.max_list.append(float(row['TMAX']))
                else:
                    self.max_list.append(self.max_list[-1])

        def minTemp(self,row):
            if row['STID'] == self.stid:
                if float(row['TMIN']) != -996.00:
                    self.max_list.append(float(row['TMIN']))
                else:
                    self.max_list.append(self.min_list[-1])

        def humidity(self,row):
            if row['STID'] == self.stid:
                if float(row['HAVG']) != -996.00:
                    self.max_list.append(float(row['HAVG']))
                else:
                    self.max_list.append(self.humid[-1])
        
        def findWMax(self,row):
            if row['STID'] == self.stid:
                if float(row['WSMX']) != -996.00:
                    self.max_list.append(float(row['WSMX']))
                else:
                    self.max_list.append(self.windMax[-1])

        def findWMin(self,row):
            if row['STID'] == self.stid:
                if float(row['WSMN']) != -996.00:
                    self.max_list.append(float(row['WSMN']))
                else:
                    self.max_list.append(self.windMin[-1])

        def findRain(self,row):
            if row['STID'] == self.stid:
                if float(row['RAIN']) != -996.00:
                    self.max_list.append(float(row['RAIN']))
                else:
                    self.max_list.append(self.rain[-1])
    
    altu = Station("ALTU", 1)
    beav = Station("BEAV", 2)
    nrmn = Station("NRMN", 3)
    tish = Station("TISH", 4)
    tuln = Station("TULN", 5)

    stations = [altu, beav, nrmn, tish, tuln]


    input("Welcome to weather charts {press any key to continue}")

    name = input("what is your name? -->  ")
    print("which station?")
    for station in stations:
        print(f"{station.stid}[{station.index}]")
    
    sChoice = int(input("-->  "))
    for station in stations:
        if sChoice == station.index:
            sChoice = station

    print("what do you want to see")
    print("MaximumTempurature[1]")
    print("MinimumTempurature[2]")
    print("Humidity[3]")
    print("Minimum wind speed[4]")
    print("Maximum wind speed[5]")
    print("Rain[6]")
    
    wChoice = int(input("-->  "))
    
    if wChoice == 1:
        for row in reader:
            sChoice.maxTemp(row)
    elif wChoice == 2:
        for row in reader:
            sChoice.minTemp(row)
    elif wChoice == 3:
        for row in reader:
            sChoice.humidity(row)
    elif wChoice == 4:
        for row in reader:
            sChoice.findWMax(row)
    elif wChoice == 5:
        for row in reader:
            sChoice.findWMin(row)
    elif wChoice == 6:
        for row in reader:
            sChoice.findRain(row)
    
    days_x = []
    for i in range(366):
        days_x.append(i)
    
    print(sChoice)

    plt.plot(days_x, sChoice.max_list, label = sChoice.stid)

    plt.xlabel('day of the year')
    plt.ylabel('tempurature in degrees')
    plt.title('tempurature lol')
    plt.show()
                    