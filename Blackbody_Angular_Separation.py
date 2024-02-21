#Angular Separation and Uncertainty

import math

def read_file_to_list(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            if len(numbers) == 3:
                try:
                    result.append([float(numbers[0]), float(numbers[1]), float(numbers[2])])
                except ValueError:
                    print(f"Warning: Couldn't convert {line.strip()} to floats.")
    return result


def write_list_to_file(data, filename):
    #writes the treated data to a new text file for plotting
    for sublist in data:
        if len(sublist) != 3:
            print(f"Warning: The sublist {sublist} does not have 4 elements. Skipping...")
            continue

        with open(filename, 'a') as file:
            file.write(f"{sublist[0]}\t{sublist[1]}\t{sublist[2]}\n")

def error_propegation(delta):
    res = ((delta**2)+(0.5))**0.5
    return res

def angular_sep(List):
    List.append(["","",""])
    data = []
    i = 0
    while (List[i] != ["","",""]):
        V = List[i][0]
        A = 78.7 - List[i][1]
        D = error_propegation(List[i][2])
        data.append([V,A,D])
        i += 1
    return data

filename1 = "Reduced_peak_position_final.txt" #single slit data file
filename2 = "Angular_Peak_Separation_Data_Final.txt" #new text file name

data = read_file_to_list(filename1)

data1 = angular_sep(data)

print(data1)
write_list_to_file(data1, filename2)




