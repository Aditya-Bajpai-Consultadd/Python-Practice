#Develop a program that splits functionality into three separate
#modules: one for fetching data (e.g., reading a file), one for
#processing (e.g., filtering or transforming the data), and one for
#reporting results (e.g., saving or displaying the output).

#This is the reading file for CSV

import pandas as pd

def read_file(path):
    file  = pd.read_csv(path,encoding = 'latin1')
    return file