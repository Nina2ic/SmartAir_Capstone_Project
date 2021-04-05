# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import pyrebase
import time
from time import sleep
import board
import adafruit_dht
#!/usr/bin/env python3
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711




# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)


    
    

config = {
  # You can get all these info from the firebase website. It's associated with your account.
  "apiKey": "AIzaSyAlX75Wolc_9HanzlN7Kl7lyQfxT3r60Q4",
  "authDomain": "smartair-54180.firebaseapp.com",
  "databaseURL": "https://smartair-54180-default-rtdb.firebaseio.com/",
  "storageBucket": "smartair-54180.appspot.com"
}
user = None

def GetAuthorized(firebase):
    global user
    auth = firebase.auth()  # Get a reference to the auth service
    # authenticate a user
    try:
        user = auth.sign_in_with_email_and_password("airsmart91@gmail.com",
                                                    "123456")  # username and password of your account for database
        print(user)  # display the user information, if successful
    except:
        print("Not authorized")
        user = None

# The function to initialize the database.
# ====================================================================================================
def dbInitialization():
    firebase = pyrebase.initialize_app(config)  # has to initialize the database
    GetAuthorized(firebase)  # get authorized to operate on the database.
    return firebase

# The function to get the data from firebase database.
# ====================================================================================================
def GetDatafromFirebase(db):
    results = db.child("data").get(user["idToken"]).val();  # needs the authorization to get the data.
    print("These are the records from the Database")
    print(results)
    return;

# The function to send the data to firebase database.
# ====================================================================================================
def sendtoFirebase(db, sensordata):
    result = db.child("data").push(sensordata, user["idToken"])  # needs the authorization to save the data
    print(result)
    return;


# The function to send the data to firebase database's user authorized section.
# Each user has a separate record tree, and it is only accessible for the authorized users.
# ====================================================================================================
def sendtoUserFirebase(db, sensordata):
    userid = user["localId"] # this will guarantee the data is stored into the user directory.
    result = db.child("userdata").child(userid).push(sensordata, user["idToken"])  # needs the authorization to save the data
    print(result)
    return;

# The function to set up the record structure to be written to the database.
# ====================================================================================================
def setupData(temp, humidity, timestamp, weight):
    sensor = {"temperature": temp,
              "humidity": humidity,
              "weight": weight,
              "timestamp": timestamp}  # always post the timestamps in epoch with the data to track the timing.
    # Store the data as the dictionary format in python  # refer to here:
    # https://www.w3schools.com/python/python_dictionaries.asp
    return sensor

def loadIt():
#     GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    # Create an object hx which represents your real hx711 chip
    # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
    doutS = str(board.D14)
    pdS = str(board.D15)
    dout = int(doutS)
    pd = int(pdS)
    hx = HX711(dout_pin=dout, pd_sck_pin=pd)
    # measure tare and save the value as offset for current channel
    # and gain selected. That means channel A and gain 128

    err = hx.zero()
    print(err)
    # check if successful
    if err:
        raise ValueError('Tare is unsuccessful.')

    reading = hx.get_raw_data_mean()
    if reading:  # always check if you get correct value or only False
        # now the value is close to 0
        print('Data subtracted by offset but still not converted to units:',
              reading)
    else:
        print('invalid data', reading)
    
    return hx
# def loadCell():
#     try:
#         
#         GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
#         # Create an object hx which represents your real hx711 chip
#         # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
#         hx = HX711(dout_pin=14, pd_sck_pin=15)
#         # measure tare and save the value as offset for current channel
#         # and gain selected. That means channel A and gain 128
#         
#         err = hx.zero()
#         # check if successful
#         if err:
#             raise ValueError('Tare is unsuccessful.')
# 
#         reading = hx.get_raw_data_mean()
#         if reading:  # always check if you get correct value or only False
#             # now the value is close to 0
#             print('Data subtracted by offset but still not converted to units:',
#                   reading)
#         else:
#             print('invalid data', reading)
# 
#         # In order to calculate the conversion ratio to some units, in my case I want grams,
#         # you must have known weight.
#        
#         #input('Put known weight on the scale and then press Enter')
#         #reading = hx.get_data_mean()
#     #     if reading:
#     #         print('Mean value from HX711 subtracted by offset:', reading)
#     #         known_weight_grams = input(
#     #             'Write how many grams it was and press Enter: ')
#     #         try:
#     #             value = float(known_weight_grams)
#     #             print(value, 'grams')
#     #         except ValueError:
#     #             print('Expected integer or float and I have got:',
#     #                   known_weight_grams)
# 
#             # set scale ratio for particular channel and gain which is
#             # used to calculate the conversion to units. Required argument is only
#             # scale ratio. Without arguments 'channel' and 'gain_A' it sets
#             # the ratio for current channel and gain.
#     #         ratio = reading / value  # calculate the ratio for channel A and gain 128
#         ratio = 221.394
#         hx.set_scale_ratio(ratio)  # set ratio for current channel
#         print('Ratio is set.', ratio)
#     #     else:
#     #         raise ValueError('Cannot calculate mean value. Try debug mode. Variable reading:', reading)
# 
#         # Read data several times and return mean value
#         # subtracted by offset and converted by scale ratio to
#         # desired units. In my case in grams.
#         print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
#     #     input('Press Enter to begin reading')
#         print('Current weight on the scale in grams is: ')
#         
#         weight = hx.get_weight_mean()
#         hx.reset()
#         print(weight)
#         return weight
# 
#     except (KeyboardInterrupt, SystemExit):
#         print('Bye :)')
# 
#     finally:
#         GPIO.cleanup()

def main():
    try:
        count = 0
        firebase = dbInitialization()
        hx = loadIt()
        
        ratio = 221.394
        hx.set_scale_ratio(ratio)  # set ratio for current channel
        print('Ratio is set.', ratio)
        while True:
            try:
                # Print the values to the serial port
                temperature_c = dhtDevice.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = dhtDevice.humidity
                
                
                print('Current weight on the scale in grams is: ')
            
                weight = hx.get_weight_mean()
                hx.reset()
                print(weight)
                
                
                load = weight
                print(
                    "Temp: {:.1f} F / {:.1f} C    Humidity: {}%    Weight: {} ".format(
                        temperature_f, temperature_c, humidity, load
                    )
                )
                
                temp = str(temperature_c) + " C"
                humid = str(humidity) + "%"
                percent = (load / 1000) * 100
                x = round(percent, 2) 
                loadPercent = str(x) + "%"
                print(loadPercent)
                sensordata = setupData(temp,
                                   humid,
                                   int(time.time()),
                                    loadPercent)
                sendtoFirebase(firebase.database(), sensordata)  # save to the public access data tree
                sendtoUserFirebase(firebase.database(), sensordata) # save to the user specific userdata tree   
                count += 1
                sleep(10)
                print ("Analog Signal Generated from D/A Output")
                if (count == 4):    # exit the program after 10 readings. 
                 dhtDevice.exit()
                 break;
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                dhtDevice.exit()
                raise error
        GetDatafromFirebase(firebase.database())  # this statement is outside the while loop  
    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

    finally:
        GPIO.cleanup()
        time.sleep(2.0)
    
if __name__=="__main__":
   main()