import numpy as np
import os

sac_data_dir = "/home/xubuntu/Desktop/sensor_data/labelled_vanilla"
output_dir = "/home/xubuntu/Desktop/temp_fall_detection/temp"

for each_file in os.listdir(sac_data_dir):
    each_file_dir = os.path.join(sac_data_dir, each_file)
    input_array = np.load(each_file_dir, allow_pickle=True)
    
    for each_frame in input_array[0]:
        const = np.amax(each_frame) * 0.4
        frame_shape = each_frame.shape
        each_frame += 0.5*(np.random.normal(loc=const, scale=0.7*const, size=(frame_shape[0], frame_shape[1])))

    output_file_dir = os.path.join(output_dir, each_file)
    np.save(output_file_dir, input_array, allow_pickle=True)
