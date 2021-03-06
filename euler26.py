print("Euler 26: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.")
numerator = 100**1000
biglen = 1
#iterate through range to find d. Create list of the numbers in the decimal value of the fraction. Avoid float limitations by increasing the numerator until all lengths of patterns can be evaluated, but not so much to make the runtime excessive. Trial and error until biglen stabilizes...
for each in range(2,1000):
  worker = list(str(numerator//each))
  pattern = "missing"
  while pattern == "missing":
    for item in range(1,(len(worker)//2)):
      #iterate through groupings of indices until a successive pair is found. i.e. the repeating pattern...
      if pattern == "missing" and worker[:item] == worker[item:(item*2)]:
        pattern = "found"
        pat = len(worker[:item])
        if pat > biglen:
          biglen = pat
          winner = each
    if pattern == "missing":
      worker.pop(0)
      #account for leading digits in decimal value that are not part of repeating pattern. For example: 1/81 repeating pattern doesn't start until 9 decimal places in... 
    if len(worker) == 0:
      print("error on " + str(each))
      #this should have raised errors if the numerator wasn't large enough to identify a pattern. Not sure why it doesn't seem to function...
print("The longest recurring cycle is " + str(biglen) + " digits long")
print("It is produced by 1/" + str(winner) + ". So " + str(winner) + " is your winner")
