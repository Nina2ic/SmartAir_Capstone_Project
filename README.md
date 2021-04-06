# SmartAir_Capstone_Project

<h2>Introduction</h2>

 The Smart Air  Humidifier project needed hardware parts such as different sensors, mainly DHT22 Temperature and Humidity Sensor, Load Cell, Hx711, Student lab kit and the development platform, Raspberry pi. The responsibility is shared amongst each group member to assemble hardware and make sure sensors were functioning on their own before it is connected to the firebase. The list of items needed for this project, corresponding cost and the total cost are listed below.


<h2>Items to purchase	Cost per hardware</h2>

- Raspberry pi kit	114.47<br>
- DHT22 Sensor	36.11<br>
- Hx711 Load cell Amplifier	16.11<br>
- Fusion PCB	30.94

ToTal	197.63


![image](https://user-images.githubusercontent.com/71288104/113669395-b49bf780-9681-11eb-932d-90d944bcd05d.png)


<h2>Duration of time spent on each part of the project</h2>

- Raspberry pi an estimate of 3 weeks<br>
- Dht22 sensor an estimated time of 5 weeks<br>
- Hx711 loadcell amplifier an estimated time on two week

The estimated time to complete this project is by week fourteen. Acquiring the necessary parts, PCB printing and PCB soldering perform a significant function in completing the project. Also, having any relevant experience with any of the elements as mentioned above will reduce the duration of spent on each part completion time



<h2>Designed circuit Diagram</h2>
RPI to connect to power the sensor with a 3.3v pin for my development board.  Added a 10K pull-up resistor(R2) to the power pin 1, then from R2 to Vcc. Pin 4 of the sensor is connected to the ground. The data signal directly connects the digital signal and is connected by a 1Km ohm resistor with VCC. It is something like Digital> 1Km ohm > VCC. 
•	GPI04 to pin 1
•	Connect Wire from RPI to GND

![image](https://user-images.githubusercontent.com/71288104/113535108-85fa2000-95a0-11eb-8615-fc65a61609d8.png)





<h2>Hardware Procedures and diagram</h2>
<h4>PCB design</h4>

After the completion of the schematics' final version, and chose the correct components and packaging. Merge design with my group, then Exported for PCB, then select Extended Gerber (RS-274X)… to export the PCB to a Gerber file package, which SEED fabrication facilities used to build the PCB—also, double-checked the Design from SEEED Fusion.

<h4>Raspberry pi 4</h4>

The target was developing and executing programs: the Raspberry Pi Model 4(RPI), an ARM microprocessor, and uses the Raspbian version of Linux. At the same time, It is accessible remotely over a network connection.  In this project, explore remote access using various command lines and GUI utilities and mount a USB key to store codes in the Real VNC when a connection is set up with RPI.
Raspberry pi features

![image](https://user-images.githubusercontent.com/71288104/113535251-e38e6c80-95a0-11eb-923d-12738af6ff41.png)



<h2>Remote Connection</h2>

At present, we developed our prototype using PCB, sensors, load cell amplifier and Raspberry pi
 Use the USB-to-Ethernet adapter, execute the setup software for the Startech adapter device located on my computer. After the driver installs, plug in the USB-to-Ethernet adapter. Once the device is installed, connect the network cable from the adapter to the RPI Ethernet port. Plugin the power to the RPI, then I  follow my laptop's network status as it finds this device.  In the end, it was connected to an 'Unidentified' network that doesn't have access to the internet.
Start VNC or PuTTY remote terminal program and use my RPI IP address that belongs to the router in use to establish the initial login connection
  

<h4>Raspberry pi setup</h4>
Insert a micro SD in the card reader; then, connect the card reader to the computer(new SD, no need to format). Downloaded the RPI OS, follow the instructions. After downloading, I inserted a micro SD card into the card slot on the raspberry pi underside. In the putty terminal, install the RPI operating system with the command Sudo apt-get install. Furthermore, use the WinSCP program to transfer files to the RPI


<h4>VNC</h4>
The standard release of Raspian has Real VNC remote access server software installed, which is enabled on  RPI. It can also be used to create a link to another computer's GUI over a network. To access and RPI desktop GUI: Download and execute the Real VNC viewer installation software. The connection window enters the IP address 192.168.0.19 Authenticate to the VNC server. When successful, a window open showing the RPI desktop.


<h4>DHT22 Sensor</h4>
The DHT22 is a necessary, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air and spits out a digital signal on the data pin (no analog input pins are needed). It's relatively simple to use but requires careful timing to grab data. The only real downside of this sensor is you can only get new data from it once every 2 seconds, so when using our library, sensor readings can be up to 2 seconds old. Connect the first pin on the left to 3-5V power, the second pin to your data input pin, and the rightmost pin to the ground.



![image](https://user-images.githubusercontent.com/71288104/113535388-41bb4f80-95a1-11eb-9891-7d999342c624.png)

•	3 to 5V power and I/O<br>
•	2.5mA max current use during conversion (while requesting data)<br>
•	Good for 0-100% humidity readings with 2-5% accuracy<br>
•	Good for -40 to 80°C temperature readings ±0.5°C accuracy<br>
•	No more than 0.5 Hz sampling rate (once every 2 seconds)<br>
•	Body size 27mm x 59mm x 13.5mm (1.05" x 2.32" x 0.53")<br>
•	Four pins, 0.1" spacing<br>

Weight (just the DHT22): 2.4g


<h4>Load cell Amplifier</h4>

Load Cell Amplifier is a small breakout board for the HX711 IC that quickly reads load cells to measure weight. By connecting the Amplifier to the RPI, one will be able to read the changes in the resistance of the load cell, and with some calibration, one will be able to get very accurate weight measurements. 
The HX711 uses a two-wire interface (Clock and Data) for communication. Any  GPIO pins should work, and numerous libraries have been written, making it easy to read data from the HX711. Check the hookup guide below for more information.
•	Red (Excitation+ or VCC)
•	Black (Excitation- or GND)
•	White (Amplifier-, Signal- or Output-)
•	Green (A+, S+ or O+)
•	Yellow (Shield)
Double-check to make sure all pins are connected to correct colour codes. Place the Amplifier directly on its slot on PCB or use the breadboard and secure the correct wires to the PCB

![image](https://user-images.githubusercontent.com/71288104/113670994-c8e0f400-9683-11eb-8595-afc1fbfe11e3.png)

![image](https://user-images.githubusercontent.com/71288104/113671155-fb8aec80-9683-11eb-890d-2c340d6239f7.png)



<h2>Configurations</h2>


<h4>Raspberry pi/Database</h4>

Issues with the raspberry connection setup to the VNC server:
The problem was,  unable to establish a connection between my RPI, Putty, and VNC. It displays "connection time out," even though it followed the RPI setup steps correctly. An additional steps to get it connected.
To fix it, An access to   SD card boot partition(Boot G), create a file name wpa_supplicant .conf, then paste this code into the file created


![image](https://user-images.githubusercontent.com/71288104/113535643-00776f80-95a2-11eb-971f-2ca4b5282f90.png)

Once the wifi credentials, country, SSID, and password filled in, the wifi credentials enabled the wifi connection. Also had to allow the ssh. Created another empty file in the boot G and named it SSH, then delete the txt extension. The first boot set the ssh, which establishes the connection between my RPI and putty

The DHT22 sensor stopped working; it Couldn't show the reading from the hardware to RPI; hence there was a need for a replacement. Troubleshoot was initiated to make sure the hardware connection is correct. 
In the  downloaded directory,  install the Adafruit_DHT package by using the following command on Pi:
sudo python setup.py install
or
sudo python3 setup.py install
 After the hardware was replaced, an actual reading was established and then modified the python codes as shared on GitHub. It took quite a lot of time to figure that out.
The load cell wasn't given accurate reading; after calibration, it doesn't give the same value but rather fluctuates. However, the python codes are correct.  During the course of nailing the load cell with 3D printed covers, it got damaged somehow.  With the replacement, it gives an accurate reading and stops after 2 seconds. 


<h2>Database setup Procedures<h2>
 Double-check to make sure the Laptop/PC can communicate with Firebase
To establish a firebase connection, download Pycharm EDU from here: 
 https://www.jetbrains.com/pycharm-edu/
 
 Try to make the code connect to Firebase from a PC, and use the PyCharm EDU IDE to debug the python code:
a. Install the pyrebase4 by using the following command in the project terminal: pip3 install pyrebase4 
b. Log on to the Firebase, find your project and then find the setting configurations. 
c. Set up the access rules of the database access. 
d. Follow the instructions listed on the pyrebase help page and create the connections with the proper configuration

#import pyrebase 
#Configuration of the Firebase 
config = { 
"apiKey": "apiKey", 
"authDomain": "projectId.firebaseapp.com", 
"databaseURL": "https://databaseName.firebaseio.com", 
"storageBucket": "projectId.appspot.com" 
} 
firebase = pyrebase.initialize_app(config) #initialize the connection 

To send data to the Firebase

 # Get a reference to the auth service 
auth = firebase.auth() 
# Log the user in 
user = auth.sign_in_with_email_and_password(email, password) 
# Get a reference to the database service 
db = firebase.database() 
# data to save 
data = { 
"name": "Mortimer 'Morty' Smith" 
} 
# Pass the user's idToken to the push method 
results = db.child("data").push(data, user['idToken']) 
# The following code send the data to the user’s private data area. Only authorized user should be able to get the user’s localId and write/read the data in this area. 
results = db.child("userdata").child(user["localId"]).push(data,user['idToken']) 



Raspberry pi connection to Firebase

	On Raspberry Pi, install the pyrebase4 first: 
	pip3 install pyrebase4

	Make sure your existing code can collect the data from your sensor

	Merge the PC Python code functions (GetAuthorized, dbInitialization, GetDatafromFirebase, sendtoFirebase, sendtoUserFirebase, setupData) in the demo code to your existing hardware code
	Update the function setupData to your specific needs and try to send data to the Firebase. Refer to the code posted on the blackboard for this part

https://github.com/thisbejim/Pyrebase



<h2>Andriod App building instructions<h2>
 
 GitHub link: https://github.com/Nina2ic/SmartAir_Capstone_Project.git
	This App is designed to allow the User to control their intelligent humidifiers and remotely monitor data about the air quality and temperature inside their homes over wifi
	Allows User to set a timer on Humidifier, auto turn off the device when desired quality is achieved.
	Remote turn on the device from anywhere
	Notifies User when the water level is low
	Notifies user when the filter is ready to be changed
	Connects to multiple devices

Realtime Database Storage

	The name and model number of each device is also stored in the Firebase
	realtime database under the name "Devices."
	It is also stored in the username, email address, and age of each user authenticated by Firebase in another "Users" field
Fig 6

 



First of all, design  pages using Adobe XD then import to Andriod studio. Locate the projectsprojects folder in the open ListmakerListmaker App inside the starterstarter folder. 

For the first time to open the project, Android Studio takes a few minutes to set up the environment and update its dependencies.

With the Listmaker project open in Android Studio, run the project using a device or emulator.

Creating lists is an important action in Listmaker, making sense to use a FAB to add new lists. The FAB icon doesn't convey the Activity of creating a new list, so the first task is to select an appropriate icon. adding 

Open activity_main.xmlactivity_xml, and in the Component TreeComponent Tree window, select the Floating Action ButtonFloating Button.

Adding a DialogAdding Dialog

When users tap the FAB in Listmaker, you want the button to open a Dialog to enter a name for their new list. The Dialog will contain labels toWhen toprompt users for information.prompt 

Rather than hardcoding these prompt strings, you'll add these strings to strings.xmlstrings.xml. This keeps the strings for Listmaker in one place, making it easier to. toupdate the strings or to support another language in the future.update 

Open strings.xmlstrings.xml and add the following strings: 
<<stringstring name= "name_of_list""list">What isis the name of your list?</ stringstring>> <<stringstring name= "create_list""list">Create</>Create</stringstring>> 

Open MainActivity.ktMainActivity.kt. At the bottom of the file, add a method to create an AlertDialogAlertDialog to get the name of the list from the user: 
privateprivate funfun showCreateListDialogshowCreateListDialog()() { // 1// 1 valval dialogTitle = getString(R.string.name_of_list) valval positiveButtonTitle = getString(R.string.create_list) // 2// 2 valval builder = AlertDialog.Builder( thisthis)) valval listTitleEditText = EditText( thisthis)) listTitleEditText.inputType = InputType.TYPE_CLASS_TEXT builder.setTitle(dialogTitle) builder.setView(listTitleEditText) // 3// 3 builder.setPositiveButton(positiveButtonTitle) { dialog, _ -> dialog.dismiss() } // 4// 4 builder.create().show()


}} 

With this method, Retrieve the strings you defined in strings.xmlstrings.xml for use in the Dialog. 


Create an AlertDialog.BuilderAlertDialog.Builder to help construct the Dialog. An EditTextEditText View is created to serve as the input field for the user to enter the name of ofthe list.the 
The inputTypeinputType of the EditTextEditText is set to TYPE_CLASS_TEXTTYPE_TEXT. Specifying the input type gives Android a hint that the most appropriate keyboard to show is.. is.In this case, a text-based keyboard, since you want the list to have a name.
The title of the Dialog is set by calling setTitlesetTitle. You also set the content View of the Dialog. In this case the EditTextEditText View, by calling setViewsetView..


Add a positive buttonpositive button to the Dialog; this tells the Dialog a positive action has occurred and something should happen. 
You pass in positiveButtonTitlepositiveButtonTitle as the label for the button and implement an onClickListeneronClickListener. 
Finally, instruct the Dialog Builder to create the Dialog and display it on the screen.

Now that you have code to show the Dialog, you need to call it when the user taps the FAB. Locate the setOnClickListenersetOnClickListener called on fabfab inside onCreateonCreate..Replace the contents of the OnClickListenerOnClickListener with a call to the new method: 
fab.setOnClickListener { showCreateListDialog() }} 

Run the App and tap on the pink FAB in the bottom-right of the screen. It will display the Create List Dialog as expected.



Creating a listCreating list

Start by creating a model for a list to use throughout the App.

In the Project navigator, Right-click com.raywenderlich.listmakercom.listmaker. In the options that appear, select New ▸ Kotlin File/ClassNew Class



Android Studio creates and displays the new class. Next, add a primary constructor to TaskList.ktTaskList.kt so it can be given a name and a list of associated tasks: 
classclass TaskListTaskList((valval name: String, valval tasks: ArrayList<String> = ArrayList()) { }} 

Next, find a way need a way to save the list to the device. One can do this by using SharedPreferencesSharedPreferences.


 




Hooking up the ActivityHooking Activity


Open MainActivity.ktMainActivity.kt and initialize a property to hold the ListDataManagerListDataManager::
valval listDataManager: ListDataManager = ListDataManager( thisthis)) 

This creates a new ListDataManagerListDataManager as soon as the Activity is created. 

Next, update the positive button’s onClickListeneronClickListener in showCreateListDialog() to add create a list and save it to the ListDataManagerListDataManager::
builder.setPositiveButton(positiveButtonTitle) { dialog, _ -> val listlist = TaskList(listTitleEditText.text.toString()) listDataManager.saveList( listlist)) val recyclerAdapter = listsRecyclerView.adapter as ListSelectionRecyclerViewAdapter recyclerAdapter.addList( listlist)) dialog.dismiss() }} 

Take the name of the list and create an empty TaskListTaskList to save to SharedPreferences, then get the adapter of the RecyclerView and cast it as the custom customadapter adapter ListSelectionRecyclerViewAdapterListSelectionRecyclerViewAdapter began earlier. 

Using the adapter, pass the TaskListTaskList into the adapter using addListaddList, so it knows it has something to show. Don't worry about the Unresolved referenceUnresolved referenceerror on addListaddList; It will be created this method shortly.

In the onCreateonCreate method of MainActivity.ktMainActivity.kt, replace the set up code for the RecyclerView starting with:, with:
// 1// 1 valval lists = listDataManager.readLists() listsRecyclerView = findViewById<RecyclerView>(R.id.lists_recyclerview) listsRecyclerView.layoutManager = LinearLayoutManager(thisthis)) // 2// 2 listsRecyclerView.adapter = ListSelectionRecyclerViewAdapter(lists) 

Going through the code step by step:
	
 Get a list of TaskListTaskLists from listDataManagerlistDataManager, ready for use., use. The RecyclerView Adapter has a source of information to display; a few changes need to be made to ensure everything works with the new lists.

Open ListSelectionRecyclerViewAdapter.ktListSelectionRecyclerViewAdapter.kt and update the class definition to accept an ArrayListArrayList of TaskListTaskList in its primary constructor: 
classclass ListSelectionRecyclerViewAdapterListSelectionRecyclerViewAdapter((privateprivate valval lists : ArrayList<TaskList>) : RecyclerView.Adapter<ListSelectionViewHol 

Find onBindViewHolder() and update it to use the list to populate the ViewHolder instead of the static array of strings: 
overrideoverride funfun onBindViewHolderonBindViewHolder(holder: ListSelectionViewHolderListSelectionViewHolder, position: IntInt)) { holder.listPosition.text = (position + 11).toString()).toString()


holder.listTitle.text = lists. getget(position).name(name }} 

Modify getItemCount() to get the size of listslists::
overrideoverride funfun getItemCountgetItemCount()(): IntInt { returnreturn lists.size }} 

Finally, create the addList() method you called from MainActivityMainActivity to let the adapter know you have a new list to display. Add the following code to the bottom bottomof the Adapter class:of 
funfun addListaddList(list: TaskListTaskList)) { // 1// 1 lists.add(list) // 2// 2 notifyItemInserted(lists.size- 11)) }

 
<h2>Test/Run</h2>
 
To securely test whether the sensor is working appropriately, here is a checklist:

	All components are soldered and connected
	Use DMM to measure the resistance between my PCB board power and ground; the sensor and the load output accurate results.
	Use DMM to measure the resistance of all the connections
	placed my PCB on the CPU to make sure the direction of the board is positioned correctly.
	3.3v is connected to VCC on the Raspberry Pi to pin 1 of the DHT22
	GND is connected to pin 4 of the DHT22 and pin 7 of the Raspberry Pi
	Data Line is connected to pin 2 of the DHT22 and pin 6 of the Raspberry Pi
	Make sure there is a 10K Ohm resistor in between pin 2 & pin 1 of the DHT22
	Make sure to debug the codes and test the connectivity with hardware before establishing a connection to the database.


Note that turn on, and timer functions will be added later when hardware devices near completion




<h2>Github Links</h2>

https://github.com/Nina2ic/SmartAir_Capstone_Project.git





















