# Main script for data transformation

# Creates list of pass information
list_passes = []

# Postcondition: Opens file of interest and extracts azimuth value at maximum elevation
with open("data/ContactLocator_TLE_SAT_2.txt", "r") as file:
    print("Starting parsing\n")
    # Prints first row of text file
    row_str = file.readline()
    row = row_str[:-1]
    print(row)
    # Establishes variables
    row_ind = 1
    ele_val_max = 0.0
    # Loops through rows of txt file
    while row_str.endswith("\n"):
        # Extracts and prints content from row
        row_prev_str = row_str
        row_str = file.readline()
        row = row_str[:-1]
        print(row)
        # Ensures parsing starts on row with index of 4 which is the first row of data
        if row_ind < 5:
            # Stores information for first pass
            if row_ind == 4:
                pass_num = int(row[0:11])
                ele_val_max = float(row[76:91])
                azi_val = float(row[58:71])
                dt_sta_val = row[29:53]
            row_ind += 1
            continue
        # For case of row at EOF or 1st row of new pass as previous row was a empty divider row   
        elif row_prev_str == "\n":
            # Stores information for prev pass
            dt_end_val = dt_val
            list_passes.append([dt_sta_val, dt_end_val, azi_val])
            # Breaks loop when EOF is reached
            if row_str == "":
                break
            # Stores information for new pass
            pass_num = int(row[0:11])
            ele_val_max = float(row[76:91])
            azi_val = float(row[58:71])
            dt_sta_val = row[29:53]
            continue
        # Skips empty divider rows
        elif row == "":
            continue
        # For 2nd row of a pass onwards, checks elevation angle with that of previous value
        ele_val = float(row[76:91])
        dt_val = row[29:53]
        # Stores information on current row if max elevation thus far is reached in pass
        if ele_val > ele_val_max:
            ele_val_max = ele_val
            azi_val = float(row[58:71])
print(list_passes)
print(len(list_passes))