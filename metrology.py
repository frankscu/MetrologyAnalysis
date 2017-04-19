#!/bin/python

import csv
import numpy as np
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
def readBridgeTool(filename):
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

    path = str(filename) + ".csv"
    csv_writer_table(results,path)

    return z_pos

#----------------------------------------------------------------------
def readHybridWithoutASICs(filename):
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

    results = zip(z_pos,z_d)
    results = zip(*results)

    path = str(filename) + ".csv"
    csv_writer_table(results,path)

    zd = z_d[1:11]
    return zd

#----------------------------------------------------------------------
def average_bridge(zpos):
    zd_asic = []
    z_touchpin = np.mean(zpos[0:4])
    for i in range(1,11):
        zpos_asic = np.mean(zpos[(0+4*i):(4+4*i)])
        zd_asic.append(z_touchpin-zpos_asic)
    return zd_asic

#----------------------------------------------------------------------
if __name__ == "__main__":
    filename1 = 'set_09_laser_170410_H4.TXT'
    zpos_BridgeTool = readBridgeTool(filename1)

    filename2 = 'panelVII_20170410_H4_h2.TXT'
    zd_Hybrid = readHybridWithoutASICs(filename2)

    print(zpos_BridgeTool)
    print(zd_Hybrid)

    zd_BridgeTool = average_bridge(zpos_BridgeTool)
    print(zd_BridgeTool)
    glue_thickness = []
    for i in range(0,(len(zd_Hybrid))):
        glue_thickness.append((zd_BridgeTool[i] + zd_Hybrid[i] - 0.3)*1000)

    path = "results.csv"
    csv_writer(glue_thickness,path)
