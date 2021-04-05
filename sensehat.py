from sense_hat import SenseHat
import pyrebase
import time
from time import sleep


sense = SenseHat()
sense.set_rotation()
sense.clear()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

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
def setupData(temp, humidity, timestamp):
    sensor = {"temperature": temp,
              "humidity": humidity,
              "timestamp": timestamp}  # always post the timestamps in epoch with the data to track the timing.
    # Store the data as the dictionary format in python  # refer to here:
    # https://www.w3schools.com/python/python_dictionaries.asp
    return sensor

def main():
    count = 0
    firebase = dbInitialization()
    sense.clear(blue)
    while True:
        temp = round(sense.get_temperature(), 2)
        humidity = round(sense.get_humidity(), 2)
        print("Temp: ", temp, "Humidity: ", humidity)
        sense.show_message(str(round(temp,2)))
        sensordata = setupData(temp,
                               humidity,
                               int(time.time()))
        sendtoFirebase(firebase.database(), sensordata)  # save to the public access data tree
        sendtoUserFirebase(firebase.database(), sensordata) # save to the user specific userdata tree   
        count += 1
        sleep(10)
        print ("Analog Signal Generated from D/A Output")
        if (count == 2):    # exit the program after 10 readings. 
         break;
    GetDatafromFirebase(firebase.database())  # this statement is outside the while loop  
if __name__=="__main__":
   main()
