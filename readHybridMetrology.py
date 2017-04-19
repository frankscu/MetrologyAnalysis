#!/bin/python

import csv
#----------------------------------------------------------------------
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        for val in data:
            writer.writerow([val])

#----------------------------------------------------------------------
def csv_writer_table(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        for val in data:
            writer.writerows([val])

#----------------------------------------------------------------------

if __name__ == "__main__":
    filename = 'panelVII_20170413_H5_h2.txt'

    with open(filename) as f:
        data = f.readlines()

    f.close()

    z_pos = []
    z_d = []

    z_d.append(0) # Datum plane, no distance

    nlines = len(data)
    for line in range(nlines):
        value = data[line].split()
        if value[0]=='Z':
            print(value[3])
            z_pos.append(float(value[3]))  # z position
        elif value[0]=='ZD':
            print(value[3])
            z_d.append(float(value[3])) # z distance

    #print z_pos
    #path = "z_pos.csv"
    #csv_writer(z_pos,path)

    #print z_d
    #path = "z_d.csv"
    #csv_writer(z_d,path)

    results = zip(z_pos,z_d)
    results = zip(*results)
    print(results)

    path = "results.csv"
    csv_writer_table(results,path)


