import csv
from operator import truediv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    days_x = []
    for i in range(366):
        days_x.append(i)

    class Station():
        def __init__(self, stid, index):
            self.stid = stid
            self.max_list = []
            self.index = index
            

        def fill_list(self,row):
            if row['STID'] == self.stid:
                if float(row['TMAX']) != -996.00:
                    self.max_list.append(float(row['TMAX']))
                else:
                    self.max_list.append(self.max_list[-1])
        
    ard2 = Station("ARD2", 1)
    beav = Station("BEAV", 2)
    bois = Station("BOIS", 3)
    cent = Station("CENT", 4)
    nrmn = Station("NRMN", 5)
    stil = Station("STIL", 6)
    tish = Station("TISH", 7)
    tuln = Station("TULN", 8)
    wood = Station("WOOD", 9)

    stations = [ard2, beav, bois, cent, nrmn, stil, tish, tuln, wood]

    for row in reader:
        for station in stations:
            station.fill_list(row)


    input("Welcome to weather charts {press any key to continue}")
    choosing = "true"
    chosen = []
    print("stations: [1]ard2 [2]beav [3]bois [4]cent [5]nrmn [6]stil [7]tish [8]tuln [9]wood")
    while choosing == "true":  
        choice = int(input("which station do you wanna graph? -> "))
        if choice in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            for station in stations:
                if choice == station.index:
                    chosen.append(station)
        elif choice == 10:
            choosing = "false"
            for station in chosen:
                plt.plot(days_x, station.max_list, label = station.stid)
        else:
            print("not a choice silly head ;-)")

        print("stations: [1]ard2 [2]beav [3]bois [4]cent [5]nrmn [6]stil [7]tish [8]tuln [9]wood")
        print("[10]plot chosen stations")




plt.xlabel('day of the year')
plt.ylabel('tempurature in degrees')
plt.title('tempurature lol')
plt.show()

        
        


