"""
Applies downsampling of factor 2 without main()
"""

import os
import csv
import sys
import subprocess
import numpy as np

sys.path.append('/home/xubuntu/Desktop/Fall_Detection/ml/filters')
from downsample import downsample

prog_dir = "/home/xubuntu/Desktop/Fall_Detection/data_conversion/write_to_npy.py"
raw_fall = "/home/xubuntu/Desktop/sensor_data/raw/fall"
raw_notfall = "/home/xubuntu/Desktop/sensor_data/raw/not_fall"
vanilla_fall = "/home/xubuntu/Desktop/sensor_data/vanilla_npy/fall"
vanilla_notfall = "/home/xubuntu/Desktop/sensor_data/vanilla_npy/not_fall"
labelled_vanilla_dir = "/home/xubuntu/Desktop/sensor_data/labelled_vanilla"
downsample_dir = "/home/xubuntu/Desktop/sensor_data/downsample2"

labels_jd = "/home/xubuntu/Desktop/temp_fall_detection/labels_jd.csv"
labels_tm = "/home/xubuntu/Desktop/temp_fall_detection/labels_tm.csv"
labels_x = "/home/xubuntu/Desktop/temp_fall_detection/labels_x.csv"
labels_yc = "/home/xubuntu/Desktop/temp_fall_detection/labels_yc.csv"

"""
unlabelled_falls = []
labelled_falls = []
for each_csv in [labels_jd, labels_tm, labels_x, labels_yc]:
    with open(each_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for each_row in spamreader:
            if each_row[0] in os.listdir(vanilla_fall):
                if each_row[0] not in labelled_falls:
                    labelled_falls.append(each_row[0])
                else:
                    print(each_row[0])

for each_file in os.listdir(vanilla_fall):
    if each_file not in labelled_falls:
        unlabelled_falls.append(each_file)

labelled_but_missing = []
for each_file in labelled_falls:
    if each_file not in os.listdir(vanilla_fall):
        labelled_but_missing.append(each_file)
        

print(unlabelled_falls)
print(len(unlabelled_falls))
"""

all_vanilla = []
all_vanilla.extend(os.listdir(vanilla_fall))

not_labelled = []
for each_file in all_vanilla:
    if each_file not in os.listdir(labelled_vanilla_dir):
        not_labelled.append(each_file)


print(not_labelled)
print(len(not_labelled))



