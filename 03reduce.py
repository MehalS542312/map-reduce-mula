input = open("sortoutput.txt","r")
r = open("reduceoutput.txt", "w")

thisKey = ""
thisValue = 0.0

for line in input:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

input.close()
r.close()
