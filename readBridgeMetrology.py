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
    filename = 'set_09_laser_170323_adjust6.TXT'

    with open(filename) as f:
        data = f.readlines()

    f.close()

    x_pos = []
    y_pos = []
    z_pos = []

    nlines = len(data)
    for line in range(nlines):
        value = data[line].split()
        if value[0]=='X':
            print(value[3])
            x_pos.append(float(value[3]))  # x position#
        elif value[0]=='Y':
            print(value[3])
            y_pos.append(float(value[3]))
        elif value[0]=='Z':
            print(value[3])
            z_pos.append(float(value[3]))


    results = zip(x_pos,y_pos,z_pos)
    results = zip(*results)
    print(results)

    path = "results.csv"
    csv_writer_table(results,path)


