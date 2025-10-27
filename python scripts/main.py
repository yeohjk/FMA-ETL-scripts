# Main script for data transformation

# Postcondition: Imports required modules/packages
import csv

# Creates list of pass information
list_passes = []

# Postcondition: Opens file of interest and extracts azimuth value at maximum elevation
with open("data/ContactLocator_TLE_SAT_2.txt", "r") as file_obj:
    csv_obj = csv.reader(file_obj)
    print("Starting parsing\n")
    # Loops through rows of txt file
    row_ind = 0
    ele_val_max = 0.0
    for row in csv_obj:
        # Ensures parsing starts on row with index of 4 which is the first row of data
        if row_ind < 5:
            # Stores information for first pass
            if row_ind == 4:
                pass_num_current = int(row[0][0:11])
                ele_val_max = float(row[0][76:91])
                azi_val = float(row[0][58:71])
                dt_sta_val = row[0][29:53]
            row_ind += 1
            continue
        # Skips empty rows dividing passes
        elif row == []:
            continue
        # Continues to next loop when reached new pass
        pass_num = int(row[0][0:11])
        if pass_num > pass_num_current:
            # Stores information for prev pass
            dt_end_val = dt_val
            list_passes.append([dt_sta_val, dt_end_val, azi_val])
            # Stores information for new pass
            pass_num_current = pass_num
            ele_val_max = float(row[0][76:91])
            azi_val = float(row[0][58:71])
            dt_sta_val = row[0][29:53]
            continue
        # Checks elevation angle with that of previous value
        ele_val = float(row[0][76:91])
        dt_val = row[0][29:53]
        if ele_val > ele_val_max:
            ele_val_max = ele_val
            azi_val = float(row[0][58:71])
        print(row)
print(list_passes)