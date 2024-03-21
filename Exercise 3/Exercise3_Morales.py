"""
Exercise 3
Jannah Marc Morales
2023-03947
"""

from math import cos, radians, sin, sqrt
def getLatitude(distance,azimuth):
    '''
    Compute for the latitude of a given line
    
    Input:
    distance - float
    azimuth - float
    
    output:
    latitude - float
    '''
    latitude = -distance*cos(radians(azimuth))
    return latitude

def getDeparture(distance,azimuth):
    '''
    Compute for the departure of a given line
    
    Input:
    distance - float
    azimuth - float
    
    output:
    latitude - float
    '''
    departure = (-1*distance)*sin(radians(azimuth))
    return departure


def azimuthToBearing(azimuth):
    '''
    Compute for DMS bearing of a given angle
    
    Input:
    azimuth - float
    
    Output:
    bearing - string
    '''
    if "-" in str(azimuth): #Value in DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = int(degrees) + (int(minutes)/60) + (int(seconds)/3600)
    else:
        azimuth = float(azimuth)%360


    if azimuth > 0 and azimuth < 90:
        Az = azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'S {: ^3} W'.format(DMS)
    elif azimuth > 90 and azimuth < 180:
        Az = 180 - azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'N {: ^3} W'.format(DMS)
    elif azimuth > 180 and azimuth < 270:
        Az = azimuth - 180
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'N {: ^3} E'.format(DMS)
    elif azimuth > 270 and azimuth < 360:
        Az = 360 - azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'S {: ^3} E'.format(DMS)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        print ()


    return bearing, azimuth

counter = 1
lines = []
lines2 = []
sumLat = 0
sumDep = 0
sumDist = 0

while True:
    print()
    print("Line No. ", counter)
    distance = float(input("Distance: ")) #Input Distance
    azimuth = input("Azimuth from the South: ") #Input Azimuth
    bearing = azimuthToBearing(azimuth)
    if "-" in str(azimuth): #Value in DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = int(degrees) + (int(minutes)/60) + (int(seconds)/3600)
    else:
        azimuth = float(azimuth)%360


    if azimuth > 0 and azimuth < 90:
        Az = azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'S {: ^3} W'.format(DMS)
    elif azimuth > 90 and azimuth < 180:
        Az = 180 - azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'N {: ^3} W'.format(DMS)
    elif azimuth > 180 and azimuth < 270:
        Az = azimuth - 180
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'N {: ^3} E'.format(DMS)
    elif azimuth > 270 and azimuth < 360:
        Az = 360 - azimuth
        degrees = int(Az)
        minutes = (Az - degrees)*60
        M_WHOLE = int(minutes)
        seconds = (minutes-M_WHOLE)*60
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'S {: ^3} E'.format(DMS)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        print ()
    lat = getLatitude(azimuth=float(azimuth), distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth), distance=float(distance))

    sumLat += lat
    sumDep += dep
    sumDist += float(distance)

    # get corrected lat
    consCorrLat = -sumLat #consCorrLat is -CL 
    consCorrDep = -sumDep


# for line in lines:
    corr_lat = consCorrLat*(float(distance)/sumDist) #get correction per line, line [1] is distance
    corr_dep = consCorrDep*(float(distance)/sumDist)

    adjlat = lat + corr_lat #get adjusted latitude and departure, line [3] is lat
    adjdep = dep + corr_dep

    line = (counter, distance, bearing, lat, dep) #Store inputted values, create tuple of the line
    lines.append(line) #Add line to list

    line2 = (corr_lat, corr_dep, adjlat,adjdep)
    lines2.append(line2)

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
print("--------------------------------------------------------------------------------")
print('{: ^10} {: ^13} {: ^18} {: ^18} {: ^15}'.format("Line No.", "Distance", "Bearing", "Latitude", "Departure"))
print("--------------------------------------------------------------------------------")
for line in lines:
     print('{: ^10} {: ^14} {: ^15} {: ^18}{: ^17} '.format(line[0],line[1],line[2],round(line[3],3), round(line[4],3)))
     
print("\n")
print("--------------------------------------------------------------------------------")
print('{: ^15} {: ^23} {: ^15} {: ^15} '.format("C_Lat", "C_Dep", "Adj_Lat", "Adj_Dep"))
print("--------------------------------------------------------------------------------")
for line2 in lines2:
    print('{: ^10} {: ^20} {: ^15} {: ^15} '.format(line2[0],line2[1],line2[2],line2[3]))

print("\n")
print("-------------- LEC and REC --------------")
print("Summation of Latitude: ", sumLat)
print("Summation of Departure: ", sumDep)
print("Summation of Distance: ", sumDist)
lec = sqrt(sumLat**2 + sumDep**2)
print("LEC: ", lec)
rec = sumDist/lec
print("REC: 1: ", round(rec,-3))

print("-------------- END --------------")



