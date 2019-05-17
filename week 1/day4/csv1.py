import csv

with open("pass1.csv") as f1:
    csv_reader=csv.reader(f1,delimiter = ':')
    with open("pass2.csv","wt") as f2:
        csv_writer=csv.writer(f2,delimiter="\t")
        for row in csv_reader:
            csv_writer.writerow([row[0],row[2]])
            
            
