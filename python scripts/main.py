# Main script for data transformation

# Imports packages
from datetime import datetime

# Creates list of pass information
list_passes = []

# Defines function ETL
def ETL(sim_num_int):
    # Print statement for start
    print("Start of ETL process\n")

    # Postcondition: Opens file of interest and extracts azimuth value at maximum elevation
    with open(f"..\Sim {sim_num_int}\ContactLocator_TLE_SAT.txt", "r") as file:
        # Reads first row of text file and initialises variables
        row_str = file.readline()
        row = row_str[:-1]
        # Initialises variables
        row_ind = 1
        ele_val_max = 0.0
        # Loops through rows of txt file
        while row_str.endswith("\n"):
            # Extracts content from row
            row_prev_str = row_str
            row_str = file.readline()
            row = row_str[:-1]
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

    # Displays number of passes in raw data
    print(len(list_passes), "passes in raw data.\n")

    # Print statement for end
    print("End of ETL process")

    # Looping through list_passes
    for pass_list in list_passes:
        # Calculates and appends pass duration in seconds to pass information 
        sta_str = pass_list[0]
        sta_dt = datetime.strptime(sta_str[:-4], "%d %b %Y %H:%M:%S")
        end_str = pass_list[1]
        end_dt = datetime.strptime(end_str[:-4], "%d %b %Y %H:%M:%S")
        duration_int = (end_dt-sta_dt).seconds
        pass_list.append(duration_int)

    # Displays list_passes and number of passes in transformed data
    print(len(list_passes), "passes in transformed data.\n")

    # Loading extracted and transformed data to text file for further processing
    file_content = ["Target: SAT\n",\
            "\n",\
            "Observer: GSC2\n",\
                "Start Time (UTC)            Stop Time (UTC)               Duration (s)     Azimuth at PCA (deg)\n"]

    for row in list_passes:
        duration_str = str(row[3])
        while len(duration_str) < 3:
            duration_str = " " + duration_str
        row_str = row[0] + "    " + row[1] + "      " + duration_str + 14*" " + str(row[2]) + "\n"
        file_content.append(row_str)

    file_content += ["\n",\
                        f"Number of events : {len(list_passes)}\n",\
                        "\n",\
                        "\n"]

    with open("test_transformed_data.txt", "w") as file:
        file.writelines(file_content)

# Calls ETL function
ETL(43)