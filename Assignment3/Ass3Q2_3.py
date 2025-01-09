#This is the file for displaying the results of the transformation on the CSV



import pandas as pd

def display(path):
    file = pd.read_csv(path,encoding = 'latin1')

    j=0
    for i in file["CUSTOMERNAME"]:
        print(i)
        j+=1
        if j == 20:
            break
    
    return
   
    


