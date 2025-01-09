#This is the transformation file for the CSV

import pandas as pd

def transform(file):

    for i in range(len(file["CUSTOMERNAME"])):
        file["CUSTOMERNAME"][i] = file["CUSTOMERNAME"][i].upper()

    print("Customer's names have been made to ALL CAPS")
    file.to_csv('sales_data_sample.csv')
    return
    