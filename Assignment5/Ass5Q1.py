#Write a program to analyze a CSV file containing sales data.
#Generate a report with total sales, average sales, and the top-
#selling product.

import pandas as pd

def main():
    file  = pd.read_csv('sales_data_sample.csv',encoding = 'latin1')
    
    totalSales()
    averageSales()
    topSellingProduct()


def totalSales():
    file = pd.read_csv('sales_data_sample.csv',encoding = 'latin1')
    print("Total Sales are: ", file['SALES'].sum())
    return 
def averageSales():
    file = pd.read_csv('sales_data_sample.csv',encoding = 'latin1')
    print("Average Sales are: ", file['SALES'].mean())
    return

def topSellingProduct():
    file = pd.read_csv('sales_data_sample.csv',encoding = 'latin1')
    print("Top Selling Product is: ",file['PRODUCTCODE'].mode())
    return

main()