#Develop a program that splits functionality into three separate
#modules: one for fetching data (e.g., reading a file), one for
#processing (e.g., filtering or transforming the data), and one for
#reporting results (e.g., saving or displaying the output).

#This is the driver file for the program

import Ass3Q2_1, Ass3Q2_3, Ass3Q2_2

def main():
    file = Ass3Q2_1.read_file('sales_data_sample.csv')
    list = Ass3Q2_2.transform(file)
    Ass3Q2_3.display('sales_data_sample.csv')
    return

main()