import numpy as np
import os
import subprocess

total_elements_count = 100

labelled_npy_dir = "/home/xubuntu/Desktop/sensor_data/labelled_vanilla"
temp_dir = "/home/xubuntu/Desktop/temp_fall_detection/temp"
output_dir = "/home/xubuntu/Desktop/temp_fall_detection/top_{0}_remove_center_gif".format(total_elements_count)


def remove_center(input_array):
    data = input_array[0]
    altered_data = data[:,:63,:]
    number_of_frames = data.shape[0]
    to_concat = np.full((number_of_frames,3,128), 0)
    altered_data = np.concatenate((altered_data, to_concat), axis=1)
    altered_data = np.concatenate((altered_data, data[:,66:,:]), axis=1)

    return np.array([altered_data, input_array[1]])

def extractcoords(input_array, extracted_per_frame):
    data = input_array[0]
    label = input_array[1]
    output_data = None
    is_first = True

    if extracted_per_frame > data.shape[0]*data.shape[1]*data.shape[2]:
        exit("ERROR - extracted_per_frame more than total number of points in input data")

    for i in range(data.shape[0]):
        values_list = []
        coordinates_dict = {}
        input_frame = data[i]
        output_frame = np.full((1,128,128), 0)

        for y in range(data.shape[1]):
            for x in range(data.shape[2]):
                val = float(input_frame[y][x])
                if val != 0:
                    # if element in a frame is not zero, save its value into values_list and coordinates into coordinates_dict
                    values_list.append(val)
                    coordinates_dict[val] = coordinates_dict.get(val, [])
                    coordinates_dict[val].append([y,x])

        values_list.sort(reverse=True)

        for j in range(extracted_per_frame):
            # add coordinate values to output_data list
            value_to_extract = values_list[0]
            coordinates = coordinates_dict[value_to_extract].pop()
            output_frame[0, coordinates[0], coordinates[1]] = value_to_extract

            del values_list[0]

        if is_first:
            output_data = output_frame
            is_first = False
        else:
            output_data = np.concatenate((output_data, output_frame), axis=0)

    return np.array([output_data, label])



if __name__ == "__main__":
    # recreate temp folder
    if os.path.exists(temp_dir):
        subprocess.call("rm -rf {0}".format(temp_dir), shell=True)
        print("ERROR - folder {0} already exist. Deleting old folder...".format(temp_dir))
    os.mkdir(temp_dir)

    # recreate temp_200_remove_center_gif folder
    if os.path.exists(output_dir):
        subprocess.call("rm -rf {0}".format(output_dir), shell=True)
        print("ERROR - folder {0} already exist. Deleting old folder...".format(output_dir))
    os.mkdir(output_dir)

    for each_file in os.listdir(labelled_npy_dir):
        each_file_dir = os.path.join(labelled_npy_dir, each_file)
        input_array = np.load(each_file_dir, allow_pickle=True)
        input_array = remove_center(input_array)
        input_array = extractcoords(input_array, total_elements_count)

        if input_array[1] == 0:
            to_append = "_notfall"
        else:
            to_append = "_fall"

        output_file = each_file[:-4]+to_append+each_file[-4:]
        output_file_dir = os.path.join(temp_dir, output_file)
        np.save(output_file_dir, input_array[0], allow_pickle=True)

    # convert npy to gif
    file_list = []
    prog_dir = "/home/xubuntu/Desktop/Fall_Detection/data_conversion/npy_to_gif.py"

    for each_file in os.listdir(temp_dir):
        to_compare = each_file[:-4]
        if to_compare not in file_list:
            file_list.append(to_compare)
            print("Processing file {0}...".format(to_compare))

            subprocess.call('python3 {0} --input_folder "{1}" --input_filename "{2}" --output_folder "{3}"'.format(prog_dir, temp_dir, to_compare, output_dir), shell=True)



