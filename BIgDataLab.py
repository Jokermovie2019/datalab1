import csv

with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    class Station():
        def __init__(self, stid, maxTemp, minTemp):
            self.stid = stid
            self.maxTemp = maxTemp
            self.minTemp = minTemp

        def findPeak(self, row):
            if row['STID'] == self.stid:
                if float(row['TMAX']) != -996.00:
                    if self.maxTemp < float(row['TMAX']):
                        self.maxTemp = float(row['TMAX'])
                    if self.minTemp > float(row['TMAX']):
                        self.minTemp = float(row['TMAX'])
        
        def disp(self):
            print(f"{self.stid} max: {self.maxTemp} min: {self.minTemp}")
        
    ard2 = Station("ARD2", 0, 150)
    beav = Station("BEAV", 0, 150)
    bois = Station("BOIS", 0, 150)
    cent = Station("CENT", 0, 150)
    nrmn = Station("NRMN", 0, 150)
    stil = Station("STIL", 0, 150)
    tish = Station("TISH", 0, 150)
    tuln = Station("TULN", 0, 150)
    wood = Station("WOOD", 0, 150)

    stations = [ard2, beav, bois, cent, nrmn, stil, tish, tuln, wood]
    
    for row in reader:
        for station in stations:
            station.findPeak(row)
            
        
    for station in stations:
        station.disp()
        

    


