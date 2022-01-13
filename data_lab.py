import csv

with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    for row in reader:
        print(f"{month_list[int(row['MONTH'])-1]} {row['DAY']}, 2016; High: {row['TMAX']}, Low: {row['TMIN']}")
