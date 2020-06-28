import numpy as np
import os

input_folder_dir = "/home/xubuntu/Desktop/sensor_data/Data"
output_folder_dir = "/home/xubuntu/Desktop/sensor_data/tm_time10_doppler2_1"

for each_file in os.listdir(input_folder_dir):
    each_file_input_dir = os.path.join(input_folder_dir, each_file)
    each_file_output_dir = os.path.join(output_folder_dir, each_file)
    
    input_array = np.load(each_file_input_dir, allow_pickle=True)
    input_array = np.array([input_array[:5,:,:], 0])
    np.save(each_file_output_dir, input_array, allow_pickle=True)

print("done")
