"""
Exercise 2
Jannah Marc Morales
2023-03947
"""

# Create a sentinel controlled loop
counter = 1
lines = []
while True:
    print()
    print("Line No. ", counter)
    Distance = float(input("Distance: ")) #Input Distance
    Azimuth = input("Azimuth from the South: ") #Input Azimuth
    if "-" in Azimuth: #Value in DMS
        degrees, minutes, seconds = Azimuth.split("-")
        Azimuth = int(degrees) + (int(minutes)/60) + (int(seconds)/3600)
    else:
        Azimuth = float(Azimuth)%360


    if Azimuth > 0 and Azimuth < 90:
        Az = Azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'S {: ^3} W'.format(DMS)
    elif Azimuth > 90 and Azimuth < 180:
        Az = 180 - Azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'N {: ^3} W'.format(DMS)
    elif Azimuth > 180 and Azimuth < 270:
        Az = Azimuth - 180
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'N {: ^3} E'.format(DMS)
    elif Azimuth > 270 and Azimuth < 360:
        Az = 360 - Azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'S {: ^3} E'.format(DMS)
    elif Azimuth == 0:
        bearing = "DUE SOUTH"
    elif Azimuth == 90:
        bearing = "DUE WEST"
    elif Azimuth == 180:
        bearing = "DUE NORTH"
    elif Azimuth == 270:
        bearing = "DUE EAST"
    else:
        print ()

    line = (counter, Distance, bearing) #Store inputted values, create tuple of the line
    lines.append(line) #Add line to list

    # Ask if create new line
    yn = input("Add new line? (YES/NO) ") #Input prompt for new line
    if yn.upper() == "YES" or yn.upper() == "Y" or yn.upper() == "YEA":
        counter = counter + 1
        continue
    else:
        break
    
print("----END----")

# PRINT SMALL TABLE SHOWING LINES
print("\n\n")
print('{: ^10} {: ^10} {: ^15}'.format("Line No.", "Distance", "Bearing"))
for line in lines:
    print('{: ^10} {: ^10} {: ^15}'.format(line[0], line[1], line[2]))