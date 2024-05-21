/*
GE120: Introductory OOP for Geomatics
Jannah Marc Morales
2023-03947

Exercise 6
*/

//import packages
import React from 'react'
import { Image } from 'expo-image';
import {Picker} from '@react-native-picker/picker';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View, Button } from 'react-native';
import cute_dog_pic from './picture/cute_dog_pic.jpg'
import dms_dd from './picture/dms_dd.jpg'

export default function App() {
  
  var name = 'JANNAH'

  //setting states
  const [outputValue, setOutputValue] = React.useState('---'); //This is the default value for output
  const [inputValue, setInputValue] = React.useState('Input Value Here'); //This is the default value for input
  const [inputCase, setInputCase] = React.useState("Select Case");
  const blurhash =
  '|rF?hV%2WCj[ayj[a|j[az_NaeWBj@ayfRayfQfQM{M|azj[azf6fQfQfQIpWXofj[ayj[j[fQayWCoeoeaya}j[ayfQa{oLj?j[WVj[ayayj[fQoff7azayj[ayj[j[ayofayayayj[fQj[ayayj[ayfjj[j[ayjuayj[';

    function convertValue(value){ //function used to convert given values
      /*
      Convert the given value from DD to DMS or vice verse depending on selected case
      
      Input:
      decimal degrees - float
      degrees-minutes-seconds - string
      
      Output:
      degrees-minutes-seconds - string
      decimal degrees - float
      */
      
      if (inputCase == "1"){ //if statement for converting DD to DMS
      var degrees = Math.floor(value)
      var minutes = Math.floor((value-degrees)*60)
      var seconds = Math.round((value-degrees-(minutes/60))*3600)

      var output = degrees.toString().concat("-",minutes.toString(),"-",seconds.toString())
      setOutputValue(output)
    }
    else { //else statement, converts DMS to DD
      var elements = value.split("-")
      var output = parseFloat(elements[0]) + parseFloat(elements[1])/60 + parseFloat(elements[2])/3600
      setOutputValue(output.toPrecision(5)) //round of DD to 2 decimal places
    }
}

  return ( //Create 4 boxes inside this box, box 1 for the title, box 2 for the input, box 3 for output, box 4 for picture
    <View style={styles.box}> 
      <View style={styles.box1}>
        <Text style={styles.titleText}> Welcome to DD to DMS Calculator </Text> 
      </View> 
      <View style={styles.box2}>
        <View style={styles.boxInputCase}>
        <Text> Input Case </Text>
        <Picker
            selectedValue={inputCase}
            onValueChange={(itemValue, itemIndex) =>
              setInputCase(itemValue)
            }>
            <Picker.Item label="DD to DMS" value="1" />
            <Picker.Item label="DMS to DD" value="2" />
          </Picker>
        </View>
        <View style={styles.boxInput}>
          <TextInput  
            style={styles.input}
            onChangeText={setInputValue}
            value={inputValue}
            />
          <Button
              title="Convert"
              onPress={() =>convertValue(inputValue)}
            />
        </View>
      </View>
      <View style={styles.box3}>
        <Text style={styles.titleText}> Output: </Text>
        <Text style={styles.titleText}> {outputValue} </Text>
      </View>

      <View style={styles.box4}>
        <Image
          style={styles.image}
          source={dms_dd}
          placeholder={blurhash}
          contentFit="cover"
          transition={1000}
          />
      </View>
  
    </View>
  );
}

//style sheet for each element
const styles = StyleSheet.create({
  box: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center'
  },
  box3: {
    width: '100%',
    height: '25%',
    alignItems: 'center',
    justifyContent: 'center'
  },
  box4: {
    width: '100%',
    height: '45%',
    alignItems: 'center',
    justifyContent: 'center'
  },
  box2: {
    width: '100%',
    height: '25%',
    alignItems: 'center',
    justifyContent: 'center'
  },
  boxInputCase: {
    flexDirection: 'column',
    width: '100%',
    height: '50%',
  },
  boxInput: {
    flex: 1,
    width: '100%',
    height: '50%',
  },
  box1: {
    width: '100%',
    height: '10%',
    alignItems: 'center',
    justifyContent: 'center'
  },
  titleText: {
    fontSize: 24,
    fontWeight: '600'
  },
  image: {
    flex: 1,
    width: '100%',
    backgroundColor: '#0553',
  },
  input: {
    height: '50%',
    width: '70%',
    fontSize: 24,
    color: 'black'
  }
});
