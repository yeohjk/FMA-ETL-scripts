# Main script for data transformation

# Imports packages
from datetime import datetime

# Creates list of pass information
list_passes = []

# Print statement for start
print("Start of parsing\n")

# Postcondition: Opens file of interest and extracts azimuth value at maximum elevation
with open("..\Sim 43\ContactLocator_TLE_SAT.txt", "r") as file:
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

# Displays list_passes and number of passes
print(list_passes, "\n")
print(len(list_passes), "passes\n")

# Print statement for end
print("End of parsing")

# Looping through list_passes
for pass_list in list_passes:
    # Calculates and appends pass duration in seconds to pass information 
    sta_str = pass_list[0]
    sta_dt = datetime.strptime(sta_str[:-4], "%d %b %Y %H:%M:%S")
    end_str = pass_list[1]
    end_dt = datetime.strptime(end_str[:-4], "%d %b %Y %H:%M:%S")
    duration_int = (end_dt-sta_dt).seconds
    pass_list.append(duration_int)

# Displays list_passes and number of passes
print(list_passes, "\n")
print(len(list_passes), "passes\n")