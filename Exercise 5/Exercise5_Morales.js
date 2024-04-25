/*
GE120: Introductory OOP for Geomatics
Jannah Marc Morales
2023-03947

Exercise 5
*/

// three functions to get latitude, departure, convert azimuth to bearing
function getLatitude(distance,azimuth){ 
    /*
    Compute for the latitude of a given line
    
    Input:
    distance - float
    azimuth - float
    
    output:
    latitude - float
    */
    if (azimuth % 180 == 90) {return 0} else {
    return (-distance * Math.cos(azimuth * Math.PI / 180.0))}
}

function getDeparture(distance,azimuth){
    /*
    Compute for the departure of a given line
    
    Input:
    distance - float
    azimuth - float
    
    output:
    latitude - float
    */
    if (azimuth % 180 == 0) {return 0} else {
    return (-distance * Math.sin(azimuth * Math.PI / 180.0))}

}

function azimuthToBearing(azimuth){
    /*
    Compute for DMS bearing of a given angle
    
    Input:
    azimuth - float
    
    Output:
    bearing - string
    */

    azimuth = azimuth%360


    if (azimuth > 0 && azimuth < 90){
        bearing = 'S '.concat(azimuth.toPrecision(5).toString(), ' W')
    } else if (azimuth > 90 && azimuth < 180){
        bearing = 'N '.concat((180-azimuth).toPrecision(5).toString(), ' W')
    } else if (azimuth > 180 && azimuth < 270){
        bearing = 'N '.concat((azimuth-180).toPrecision(5).toString(), ' E')
    } else if (azimuth > 270 && azimuth < 360){
        bearing = 'S '.concat((360-azimuth).toPrecision(5).toString(), ' E')
    } else if (azimuth == 0){
        bearing = "DUE SOUTH"
    }  else if (azimuth == 90){
        bearing = "DUE WEST"
    } else if (azimuth == 180){
        bearing = "DUE NORTH"
    } else if (azimuth == 270){
        bearing = "DUE EAST"
    } else{
        print ()
    }

    return bearing
}

var data = [ //array of arrays with given data
    [13.23,  124.795],
    [15.57,  14.143],
    [43.36,  270.000],
    [23.09,  188.169],
    [10.99,  180.000],
    [41.40,  50.562]
]

var lines = [] //define empty lists to push variables into
var adjusted = []
var sumLat = 0
var sumDep = 0
var sumDist = 0

for (var i = 0; i < data.length; i++){ // for loop repeats for each line in 'data' array
    let line = data[i]
    let distance = line[0]
    let azimuth = line[1]

    let bearing = azimuthToBearing(azimuth)
    let lat = getLatitude(distance, azimuth)
    let dep = getDeparture(distance, azimuth)

    sumLat += lat
    sumDep += dep
    sumDist += distance

    lines.push([(i+1), distance, bearing, lat, dep])
}

//Print small table with line number, distance, bearing, latitude, and departure
console.log("________________________________________________________________________")
console.log()
console.log("LINE NO.".padEnd(10), 'DISTANCE'.padEnd(14), 'BEARING'.padEnd(15), 'LATITUDE'.padEnd(15), 'DEPARTURE'.padEnd(12))

console.log("________________________________________________________________________")
for (var line of lines){  // for loop repeats for each line in 'lines' array
     console.log("\n",
        line[0].toString().padStart(3).padEnd(11),
        line[1].toString().padEnd(12),
        line[2].toString().padEnd(17),
        line[3].toPrecision(5).toString().padEnd(14),
        line[4].toPrecision(5).toString().padEnd(12)
    )
}
console.log("________________________________________________________________________","\n")


// Print small table with LEC and REC
console.log("_____________________________________________________", "\n")
console.log("LEC and REC ".padStart(30))
console.log("_____________________________________________________","\n")
console.log("Summation of Latitude:", sumLat,"\n")
console.log("Summation of Departure:", sumDep,"\n")
console.log("Summation of Distance:", sumDist,"\n")
var lec = Math.sqrt(sumLat**2 + sumDep**2)
console.log("LEC:", lec,"\n")
var rec = sumDist/lec
console.log("REC: 1:"+(Math.floor(rec/1000)*1000).toPrecision(5)) //rounding the REC down to the nearest thousands

console.log("_____________________________________________________")

// Adjusting the latitude and departure using compass rule
for (var i = 0; i < data.length; i++){ // for loop repeats for each adj in 'adjusted' array
    let adj = lines[i] //loop that uses lines array as source of values
    let cLat = (-sumLat)*(adj[1]/sumDist) //adj[1] is the distance
    let cDep = (-sumDep)*(adj[1]/sumDist)
    
    let adjLat = adj[3] + cLat
    let adjDep = adj[4] + cDep

    adjusted.push([(i+1), cLat, cDep, adjLat, adjDep]) //adding corrections and adjusted latitude and departure values to a new array 
}

//Print small table with corrections and adjusted latitude and departure
console.log("________________________________________________________________________")
console.log()
console.log("LINE NO.".padEnd(14), 'C LAT'.padEnd(15), 'C DEP'.padEnd(13), 'ADJ LAT'.padEnd(15), 'ADJ DEP'.padEnd(12))

console.log("________________________________________________________________________")
for (var adj of adjusted){  // for loop repeats for each line in 'lines' array
     console.log("\n",
        adj[0].toString().padStart(3).padEnd(11),
        adj[1].toPrecision(5).toString().padEnd(15),
        adj[2].toPrecision(5).toString().padEnd(15),
        adj[3].toPrecision(5).toString().padEnd(15),
        adj[4].toPrecision(5).toString().padEnd(12)
    )
}
console.log("________________________________________________________________________","\n")
