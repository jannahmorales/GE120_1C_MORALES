class Parcel:
    def __init__(self,owner,area): #Initializing value under Parcel class
        self.owner = owner
        self.area = area

    def getClassification(self): #function to determine classification of parcel
        '''
        Determine the classification of a parcel of land
        
        input:
        area - integer
        
        output:
        classification - string
        '''
        if self.area <= 10000: 
            classification = "Residential"
       
        elif self.area > 10000 and self.area <= 120000:
            classification = "Private Agricultural"

        elif self.area > 120000:
            classification = "Public Agricultural"   

        return classification #function which returns the classification of the size of a land parcel, uses an if function to classify between three cases
    
    #overriding functions
    def __str__(self):
        print("A parcel of land owned by " + self.owner + "with an area of " + self.area + "square meters")
    def __add__(self):
        sum += self.area
        print("Consolidated lot of " + self.owner + "and " + self.owner + "with a total area of " + sum + 'square meters')

class Riparian(Parcel): #subclass of Parcel class, uses same attributes with new parameter type
    def __init__(self, type):
        self.type = type
    def getAdjoiningWaterbody(self): #function to determine the adjoining waterbody of the parcel of land
        if self.type == "1":
            waterbody = "Adjacent to River - can be subject to tilting"
          
        elif self.type == "2":
            waterbody = "Adjacent to Ocean(Littoral) - cannot be subject to tilting"
           
        else:
            waterbody = "Invalid Riparian Parcel"

        return waterbody #if function for the different cases
    
# Print defintion of parcel of land, asks for input of land owner and 
while True:
    print()
    owner = str(input("Name of Owner: ")) #Input Land Owner
    area = int(input("Lot Area (in square meters): ")) #Input area
    type = int(input("Type of Land (1 or 2: )")) #Inpu type of land
    

    #print the classification, the adjoining waterbody
