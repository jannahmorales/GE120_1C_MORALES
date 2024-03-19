"""
Long Exam 1: Direct Levelling 
Jannah Marc Morales
2023-03947

1. print a title for program
2. initialize variables
    levelling_table - tuple()
    total_distance - float +=
    tp_counter - int() 
3. def floatInput(prompt)
    input(  )
    output float(input)
4. input elevation of BM0 with floatInput
5. variable total_elevation,store running elev +=
6. while true:
    input backsight
    input foresight
    compute HI: HI = total_elevaton + BS
    distance = BS+FS
7. compute for error
    error = b
"""
# Title of program
print('{:^75}'.format("VERTICAL CONTROL SURVEY "))
print("------- Jannah Morales | This program performs direct levelling computations -------")

#Initialize variables
table = []
distance = 0
total_distance = float(distance)
tp_counter = 1

def floatInput(prompt): #Function that converts inputted values into float
    '''
    This functions asks for a numerical input and converts the value to data type, float

    Input - int
    Output - float

    '''
    convFloat = float(prompt)
    #if-else statement?
    return convFloat

def getHI(elev,bs):
    '''
    this function gets the instrument height
    input - elevation and bs, float
    output - hi
    '''
    HI = elev + bs
    return HI
def getElev(hi,fs):
    '''
    this function gets the elevation
    '''
    ELEV = hi - fs
    return ELEV

#Ask for initial elevation
print("BM 1")
BM0 = floatInput(input("Initial Elevation: "))
elev = 0
total_elevation = BM0 + elev #total elevation including initial elevation

while True:
    print("TP ", tp_counter) #label/counter for turning points
    BS = floatInput(input("Backsight Measurement (meters): "))
    FS = floatInput(input("Foresight Measurement (meters): "))

    #compute for HI
    HI = getHI(total_elevation,BS)
    print("HI: ", HI)

    elev = getElev(HI,FS)
    total_elevation += (elev - total_elevation) #running elevation of specific turning point
    print("ELEV: ", total_elevation)

    # Ask if create new line
    yn = input("Add new line? (y/n): ") #Input prompt for new line
    if yn.lower() == "yes" or yn.lower() == "y":
        tp_counter = tp_counter + 1
        continue
    else:
        break
    
print("----END----")

#printing levelling table
levelling_table = (tp_counter, BS, HI, FS, total_elevation)
table.append(levelling_table)
print("\n\n")
print('{: ^15} {: ^23} {: ^15} {: ^15} '.format("Sta.", "BS", "HI", "FS","ELEV"))
print("-------------------------------------------------------------------------------")
for levelling_table in table: #Create code where levelling table inserts BM1 and skips printing FS of first line
    print('{: ^10} {: ^20} {: ^15} {: ^15} '.format(levelling_table[0],round(levelling_table[1],6),levelling_table[2],levelling_table[3], round(levelling_table[4],6)))

error = total_elevation - BM0 #error of vertical control survey










