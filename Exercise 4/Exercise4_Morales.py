"""
GE120: Into to OOP for Geomatic Application
Jannah Marc Morales
2023-03947

Exercise 4
"""

from math import cos, radians, sin, sqrt #Import math functions from math module

class Line: 
    def __init__(self,distance,azimuth): #Initializing values under Line class
        self.distance = distance
        self.azimuth = azimuth
    
    def latitude(self): #function to get the latitude
        '''
        Compute for the latitude of a given line
        
        Input:
        distance - float
        azimuth - float
        
        output:
        latitude - float
        '''
        latitude = -float(self.distance) * cos(radians(self.azimuth))
        return latitude

    def departure(self): #function to get the departure
        '''
        Compute for the departure of a given line
        
        Input:
        distance - float
        azimuth - float
        
        output:
        departure - float
        '''
        departure = -float(self.distance)*sin(radians(self.azimuth))
        return departure

    def bearing(self): #function to get the bearing
        '''
        Compute for DMS bearing of a given angle
        
        Input:
        azimuth - float
        
        Output:
        bearing - string
        '''
        
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
        else:
            print ()


        return bearing

class Cardinal(Line): #overrides Line class
    
    def __init__(self, distance, azimuth):
        super().__init__(distance, azimuth)

    def bearing(self):
        if azimuth == 0:
            bearing = "DUE SOUTH"
        elif azimuth == 90:
            bearing = "DUE WEST"
        elif azimuth == 180:
            bearing = "DUE NORTH"
        elif azimuth == 270:
            bearing = "DUE EAST"
        else:
            print ()
        return bearing
    
# Create a sentinel controlled loop
counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

while True:
    print()
    print("Line No. ", counter)
    distance = float(input("Distance: ")) #Input Distance
    azimuth = input("Azimuth from the South: ") #Input Azimuth
    if "-" in str(azimuth): #Given value in DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = int(degrees) + (int(minutes)/60) + (int(seconds)/3600)
    else: #Given value in DD
        azimuth = float(azimuth)%360
    if azimuth % 90 == 0:
        line = Cardinal(distance,azimuth)
    else: 
        line = Line(distance,azimuth)

    sumLat += line.latitude() #the same as sumLat = sumLat + lat
    sumDep += line.departure()
    sumDist += float(line.distance)

    lines.append((counter,line.distance, line.bearing(), line.latitude(), line.departure())) #add lines to lines list

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
print('{: ^10} {: ^12} {: ^15} {: ^18} {: ^17}'.format("Line No.", "Distance", "Bearing", "Latitude", "Departure"))
print("--------------------------------------------------------------------------------")
for line in lines:
     print('{: ^10} {: ^12} {: ^15} {: ^18}{: ^17} '.format(line[0],line[1],line[2],round(line[3],3), round(line[4],3)))

print("\n")
print("-------------- LEC and REC --------------")
print("Summation of Latitude:", sumLat)
print("Summation of Departure:",sumDep)
print("Summation of Distance:", sumDist)
lec = sqrt(sumLat**2 + sumDep**2) #Compute for LEC
print("LEC:", lec)
rec = sumDist/lec #Computes for REC
print("REC: 1:", round(rec,-3)) #Print REC rounded at -3

print("-------------- END --------------")
