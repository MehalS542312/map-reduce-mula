# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 13) : 
    Id,price,brand,model,year,title_status,mileage,color,vin,lot,state,country,condition = datalist

    # print intermediate key-value pairs to standard output
    print(brand,"\t",1)
