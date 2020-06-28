import os
import csv
import subprocess

prog_dir = "/home/xubuntu/Desktop/Fall_Detection/data_conversion/npy_to_gif.py"
input_folder_fall = "/home/xubuntu/Desktop/sensor_data/vanilla_npy/fall"
input_folder_notfall = "/home/xubuntu/Desktop/sensor_data/vanilla_npy_bak/not_fall"
output_folder_fall = "/home/xubuntu/Desktop/sensor_data/gif_vanilla/fall"
output_folder_notfall = "/home/xubuntu/Desktop/sensor_data/gif_vanilla/not_fall"


input_folder = [input_folder_fall, input_folder_notfall]
output_folder = [output_folder_fall, output_folder_notfall]

print(len(prog_dir))


for i in range(2):
    file_list = []
    raw_file_list = os.listdir(input_folder[i])

    for each_file in raw_file_list:
        to_compare = each_file[:-4]
        if to_compare not in file_list:
            file_list.append(to_compare)
            print("Processing file {0}...".format(to_compare))

            subprocess.call('python3 {0} --input_folder "{1}" --input_filename "{2}" --output_folder "{3}"'.format(prog_dir, input_folder[i], to_compare, output_folder[i]), shell=True)
