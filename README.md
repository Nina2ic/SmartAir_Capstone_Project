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

<h4>Load cell Amplifier<h4>

Load Cell Amplifier is a small breakout board for the HX711 IC that quickly reads load cells to measure weight. By connecting the Amplifier to the RPI, one will be able to read the changes in the resistance of the load cell, and with some calibration, one will be able to get very accurate weight measurements. 
The HX711 uses a two-wire interface (Clock and Data) for communication. Any  GPIO pins should work, and numerous libraries have been written, making it easy to read data from the HX711. Check the hookup guide below for more information.
•	Red (Excitation+ or VCC)
•	Black (Excitation- or GND)
•	White (Amplifier-, Signal- or Output-)
•	Green (A+, S+ or O+)
•	Yellow (Shield)
Double-check to make sure all pins are connected to correct colour codes. Place the Amplifier directly on its slot on PCB or use the breadboard and secure the correct wires to the PCB



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


![image](https://user-images.githubusercontent.com/71288104/113535467-7deeb000-95a1-11eb-9f13-865893898efd.png)

![image](https://user-images.githubusercontent.com/71288104/113535478-88a94500-95a1-11eb-83de-a9c392c44c23.png)


<h2>Configurations</h2>

<h4>Hardware</h4>

<h4>Software</h4>

<h4>Raspberry pi/Database</h4>

Issues with the raspberry connection setup to the VNC server:
The problem was, I was unable to establish a connection between my RPI, Putty, and VNC. It displays "connection time out," even though it followed the RPI setup steps correctly. An additional steps to get it connected.
To fix it, An access to   SD card boot partition(Boot G), create a file name wpa_supplicant .conf, then paste this code into the file created


![image](https://user-images.githubusercontent.com/71288104/113535643-00776f80-95a2-11eb-971f-2ca4b5282f90.png)

Once the wifi credentials, country, SSID, and password filled in, the wifi credentials enabled the wifi connection. I also had to allow the ssh. Created another empty file in the boot G and named it SSH, then delete the txt extension. The first boot set the ssh, which establishes the connection between my RPI and putty. I was no longer getting the "Connection timeout" popup.



<h2>Database setup Procedures<h2>
 
 
 
<h2>Andriod App building instructions<h2>
 
 
<h2>Test/Run</h2>
 
To securely test whether the sensor is working appropriately, here is a checklist:

<b>1.</b>  3.3v is connected to VCC on the Raspberry Pi and pin 1 of the DHT22<br>
<b>2.</b>  GND is connected to pin 4 of the DHT22 and pin 7 of the Raspberry Pi<br>
<b>3.</b>  Data Line is connected to pin 2 of the DHT22 and pin 6 of the Raspberry Pi<br>
<b>4.</b>  Make sure there is a 10K Ohm resistor in between pin 2(Data Line) & pin 1(Power) of the DHT22



<h2>Github Links</h2>

https://github.com/Nina2ic/SmartAir_Capstone_Project.git





















