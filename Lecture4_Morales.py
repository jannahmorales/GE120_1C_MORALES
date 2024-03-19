# import math


# # def shout(word1, list_of_names):
# #     print(word1.upper() +word1[-3].upper()*5+ "!")
# #     print(list_of_names)

# # shout("Mafe", "Omar")
# # '''
# # given a word, get last letter, repeat 5 times
# # '''

def azimuthToBearing(azimuth):
    '''
    Compute for DMS bearing of a given angle
    
    Input:
    azimuth - float
    
    Output:
    bearing - string
    '''
    if "-" in str(azimuth): #If user inputs DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) +(float(seconds)/3600))%360
    else:
        azimuth = float(azimuth)%360

    if azimuth > 0 and azimuth < 90:
        degrees = int(azimuth)
        minutes = (azimuth - degrees)*60
        M_WHOLE = int(minutes)
        seconds = float((minutes-M_WHOLE)*60)
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'S {: ^3} W'.format(DMS)
    elif azimuth > 90 and azimuth < 180:
        azimuth = 180 - azimuth
        degrees = int(azimuth)
        minutes = (azimuth - degrees)*60
        M_WHOLE = int(minutes)
        seconds = float((minutes-M_WHOLE)*60)
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'N {: ^3} W'.format(DMS)
    elif azimuth > 180 and azimuth < 270:
        azimuth = azimuth - 180
        degrees = int(azimuth)
        minutes = (azimuth - degrees)*60
        M_WHOLE = int(minutes)
        seconds = float((minutes-M_WHOLE)*60)
        DMS = str(degrees) + "-" + str(int(minutes)) + "-" +str(round(seconds,2))
        bearing = 'N {: ^3} E'.format(DMS)
    elif azimuth > 270 and azimuth < 360:
        azimuth = 360 - azimuth
        degrees = int(azimuth)
        minutes = (azimuth - degrees)*60
        M_WHOLE = int(minutes)
        seconds = float((minutes-M_WHOLE)*60)
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
        print()

    return bearing,azimuth
