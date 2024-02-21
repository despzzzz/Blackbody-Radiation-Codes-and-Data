import math

def read_file_to_list(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            if len(numbers) == 2:
                try:
                    result.append([float(numbers[0]), float(numbers[1])])
                except ValueError:
                    print(f"Warning: Couldn't convert {line.strip()} to floats.")
    return result

def mean(List):
    #takes in a list of numbers and outputs their average
    result = 0
    for i in range(len(List)):
        result = result + List[i]
    return result/(len(List))


def standard_deviation_formula(List):
    #creates a new data point with the average value and the associated standard deviation
    result = []
    if (List != []):
        result.append(List[0][0])
        y_list = []
        sd = 0
        for i in range(len(List)):
            y_list.append(List[i][1])
        m = mean(y_list)
        for i in range (len(y_list)):
            d_squared = (y_list[i]-m)**2
            sd = sd + d_squared
        sd = (sd/len(y_list))**0.5
        result.append(m)
        result.append(0.000005)
        result.append(sd)
    return result

def reduced_data(List):
    #creates the new table of the new data points
    List.append(["",""])
    data = []
    i = 0
    while (List[i] != ["",""]):
        temp_res = []
        a = List[i][0]
        counter = 0
        while(List[i+counter][0] == a):
            temp_res.append(List[i+counter])
            counter += 1
            if (i+counter == len(List)):
                break
        d = standard_deviation_formula(temp_res)
        data.append(d)
        i += counter
        if (i == len(List)):
            break

    return data

def write_list_to_file(data, filename):
    #writes the treated data to a new text file for plotting
    for sublist in data:
        if len(sublist) != 4:
            print(f"Warning: The sublist {sublist} does not have 4 elements. Skipping...")
            continue

        with open(filename, 'a') as file:
            file.write(f"{sublist[0]}\t{sublist[1]}\t{sublist[2]}\t{sublist[3]}\n")


#Main

filename1 = "limited_area_raw.txt" #single slit data file
filename2 = "Reduced_area_under_curve.txt" #new text file name

data = read_file_to_list(filename1)
data1 = reduced_data(data)

print(data1)
#write_list_to_file(data1,filename2)