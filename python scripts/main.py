# Main script for data transformation

# Postcondition: Imports required modules/packages
import csv

# Postcondition: Opens file of interest and extracts azimuth value at maximum elevation
with open("data/ContactLocator_TLE_SAT_2.txt", "r") as file_obj:
    csv_obj = csv.reader(file_obj)
    print("Starting parsing\n")
    # Loops through rows of txt file
    row_ind = 0
    for row in csv_obj:
        # Ensures parsing starts on row with index of 4 which is the first row of data
        if row_ind < 4:
            row_ind += 1
            continue
        # Skips empty rows dividing passes
        elif row == []:
            continue
        print(row)