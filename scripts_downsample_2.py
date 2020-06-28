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
vanilla_notfall = "/home/xubuntu/Desktop/sensor_data/vanilla_npy_bak/not_fall"
labelled_vanilla_dir = "/home/xubuntu/Desktop/sensor_data/labelled_vanilla"
downsample_dir = "/home/xubuntu/Desktop/sensor_data/downsample2"

for each_file in os.listdir(labelled_vanilla_dir):
    each_file_dir = os.path.join(labelled_vanilla_dir, each_file)
    input_array = np.load(each_file_dir, allow_pickle=True)

    output0, output1 = downsample(input_array, 2)

    each_file_newdir_0 = each_file[:-4]+"_0"+each_file[-4:]
    each_file_newdir_0 = os.path.join(downsample_dir, each_file_newdir_0)
    np.save(each_file_newdir_0, output0, allow_pickle=True)
    each_file_newdir_1 = each_file[:-4]+"_1"+each_file[-4:]
    each_file_newdir_1 = os.path.join(downsample_dir, each_file_newdir_1)
    np.save(each_file_newdir_1, output1, allow_pickle=True)

    
