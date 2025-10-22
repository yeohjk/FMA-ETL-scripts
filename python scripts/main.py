# Main script for data transformation

# Postcondition: Imports required modules/packages
import csv

# Postcondition: Opens file of interest and extracts azimuth value at maximum elevation
with open("ContactLocator_TLE_SAT_2.txt", "r") as file_obj:
    csv_obj = csv.reader(file_obj)
    print("Start")
    # Postcondition: Extracts azimuth value at maximum elevation
    for i in csv_obj:
        if i == []:
            continue
        print(i)