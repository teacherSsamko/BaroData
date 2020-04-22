import csv
import os
from os import listdir

list_files = listdir("roll_list/")
print(list_files)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LIST_DIR = os.path.join(BASE_DIR, "roll_list/")

for f in list_files:
    file_csv = os.path.join(LIST_DIR, f)
    new_rows = []
    with open(file_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:
            print(' '.join(row))
            if row and row[4] != '':
                # new_line = ','.join([row[4], row[0], row[5]])
                new_line = [row[4], row[0], row[5]]
                new_rows.append(new_line)

    with open('sample.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in new_rows:
            print(row)
            writer.writerow(row)
    break
