# Extracting Data With Regular Expressions(Python 2.7.x)
import re as RE

fname = raw_input("Enter the file name:")
try:
    fhandle = open(fname)
except:
    print "File cannot be opened, now exit..."
    exit()

# Producing the sum of intergers
sum = 0
for line in fhandle:
    lst = RE.findall("[0-9]+", line)
    if len(lst) < 1: continue
    for item in lst:
        sum = sum + int(item)

print "The sum is:",sum
