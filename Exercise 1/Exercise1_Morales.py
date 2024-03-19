"""
Exercise 1
Jannah Marc Morales
2023-03947
"""

# Input Decimal Degrees
DD = 120.90347
print("Input (In Decimal Degrees):", DD)

# Get degrees
D = int(DD)
# Get minutes (integer) and minutes (whole)
M = (DD - D)*60
M_WHOLE = int(M)
# Get seconds
S = (M-M_WHOLE)*60
# Result, Print Output
DMS = [D, M, S]

print("DMS:" + str(D) + "-" + str(M_WHOLE) + "-" + str(round(S, 2)))
print() #Separator for Part 1 and Part 2

#PART2

# Input DMS
dms = "120-54-12.49"
values = dms.split("-")
print("Input (In Degrees-Minutes-Seconds):", dms)

# Converting string to integers and float data 
degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

# Conversion into DD
dd = degrees + (minutes/60) + (seconds/3600)
print("DD:", round(dd, 6))