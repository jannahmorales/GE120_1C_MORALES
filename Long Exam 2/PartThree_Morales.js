

function convertToBearing(azimuth){
        /*
        Compute for DMS bearing of a given azimuth in DMS
        
        Input:
        azimuth - string
        
        Output:
        bearing - string
        */


    
        var dms = azimuth.split("-")
        var dd = parseFloat(dms[0]) + parseFloat(dms[1])/60 + parseFloat(dms[2])/3600
        
       
        // the function converts the azimuth to dd so that it can classify between the different quadrants
        //coverts the decimal degrees to bearing, appends the directions to indicate bearing

        if (dd > 0 && dd < 90){ 
            var az = dd
            var degrees = Math.floor(az)
            var minutes = Math.floor((az-degrees)*60)
            var min = ((az-degrees)*60)-Math.floor((az-degrees)*60)
            var seconds = (min)*60
            bearing = 'S '.concat(degrees.toString().concat("-",minutes.toString(),"-",seconds.toPrecision(2).toString()), ' W')
        } else if (dd > 90 && dd < 180){
            var az = 180 - dd
            var degrees = Math.floor(az)
            var minutes = Math.floor((az-degrees)*60)
            var min = ((az-degrees)*60)-Math.floor((az-degrees)*60)
            var seconds = (min)*60
            bearing = 'N '.concat(degrees.toString(),"-",minutes.toString(),"-",seconds.toPrecision(2).toString(), ' W')
        } else if (dd > 180 && dd < 270){
            var az = dd - 180
            var degrees = Math.floor(az)
            var minutes = Math.floor((az-degrees)*60)
            var min = ((az-degrees)*60)-Math.floor((az-degrees)*60) 
            var seconds = (min)*60
            bearing = 'N '.concat(degrees.toString(),"-",minutes.toString(),"-",seconds.toPrecision(2).toString(), ' E')
        } else if (dd > 270 && dd < 360){
            var az = 360 - dd
            var degrees = Math.floor(az)
            var minutes = Math.floor((az-degrees)*60)
            var min = ((az-degrees)*60)-Math.floor((az-degrees)*60)
            var seconds = (min)*60
            bearing = 'S '.concat(degrees.toString(),"-",minutes.toString(),"-",seconds.toPrecision(2).toString(),  ' E')
        } else if (dms == 0){ //for cardinal directions
            bearing = "DUE SOUTH"
        }  else if (dd == 90){
            bearing = "DUE WEST"
        } else if (dd == 180){
            bearing = "DUE NORTH"
        } else if (dd == 270){
            bearing = "DUE EAST"
        } else{
           console.log()
        }
    
        return bearing
    
}
//Input azimuth
    azimuth = "270-00-00"
    let output = convertToBearing(azimuth)
    console.log(bearing) //print bearing


/*
The React Native components needed to develop the app are a StyleSheet, Text, TextInput, View, and Button. the StyleSheet will
contain the properties of the other components. There will be 6 boxes created using the View component, stacked upon eachother as rows
containing the following:
(1) The entire layout of the app (flex=1)
(2) The title, will use Text component, width = 100%, height = less than 20%
(3) The Input (width = 100%, height = 26%)
    (4)Box to contain text which indicates it is intended for input
    (5)the actual TextInput box where the azimuth will be entered and the Button to activate convertToBearing function
(6) Output box, uses Text element, width = 100%, height = less than 30%
*/
