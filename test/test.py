import sys
sys.path.append('src')
import src
rows = int(input("Enter the number of rows which will be printed: "))
#Making request from api and printing the rows of top most crypto currencies
src.read_API(num_rows=rows)

#if you want to store the data from the table use following algorithm
#Save the data frame retrieved from read_API() function into variable
#Use store_data function and pass this variable
#---------------stores data in CSV format------------------#
data_frame = src.read_API(num_rows=rows)
src.store_data(data_frame)  



