import csv

with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    class Station():
        def __init__(self, stid, maxTemp, minTemp):
            self.stid = stid
            self.maxTemp = maxTemp
            self.minTemp = minTemp

        def findMax(self, row):
            if row['STID'] == self.stid:
                if float(row['TMAX']) != -996.00:
                    if self.maxTemp < float(row['TMAX']):
                        self.maxTemp = float(row['TMAX'])

        def findMin(self, row):
            if row['STID'] == self.stid:
                if float(row['TMAX']) != -996.00:
                    if self.minTemp > float(row['TMAX']):
                        self.minTemp = float(row['TMAX'])

    ard2 = Station("ARD2", 0, 150)
    beav = Station("BEAV", 0, 150)

    for row in reader:
        ard2.findMax(row)
        ard2.findMin(row)

print(ard2.maxTemp)