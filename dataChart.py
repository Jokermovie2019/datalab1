import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    days_x = []
    for i in range(366):
        days_x.append(i)

    class Station():
        def __init__(self, stid):
            self.stid = stid
            self.max_list = []
            

        def fill_list(self,row):
            if row['STID'] == self.stid:
                if float(row['TMAX']) != -996.00:
                    self.max_list.append(float(row['TMAX']))
                else:
                    self.max_list.append(self.max_list[-1])
        
    ard2 = Station("ARD2")
    beav = Station("BEAV")
    bois = Station("BOIS")
    cent = Station("CENT")
    nrmn = Station("NRMN")
    stil = Station("STIL")
    tish = Station("TISH")
    tuln = Station("TULN")
    wood = Station("WOOD")

    stations = [ard2, beav, bois, cent, nrmn, stil, tish, tuln, wood]

    for row in reader:
        for station in stations:
            station.fill_list(row)
    for station in stations:
        plt.plot(days_x, station.max_list)

plt.xlabel('day of the year')
plt.ylabel('tempurature in degrees')
plt.title('tempurature lol')
plt.show()

        
        


