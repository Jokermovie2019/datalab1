import csv

with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    maxTemp = 0.0
    minTemp = 150.0
    avgMax = 0
    avgMin = 0
    listlengthTMAX = 0
    listlengthTMIN = 0

    
    for row in reader:
        if float(row['TMAX']) != -996.00:
            if maxTemp < float(row['TMAX']):
                maxTemp = float(row['TMAX'])

        if float(row['TMIN']) != -996.00:
            if minTemp > float(row['TMIN']):
                minTemp = float(row['TMIN'])

        if float(row['TMAX']) != -996.00:
            listlengthTMAX += 1
            avgMax += float(row['TMAX'])
        
        if float(row['TMIN']) != -996.00:
            listlengthTMIN += 1
            avgMin += float(row['TMIN'])

    avgMax = avgMax/listlengthTMAX
    avgMin = avgMin/listlengthTMIN

    
    print(f"Max: {maxTemp}, Min: {minTemp}")
    print(f"average max: {round(avgMax, 2)}, average min: {round(avgMin, 2)}")