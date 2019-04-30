Lab Notebook
------

__April 17, 2019__

* Orders arrived
* Allgator clip jumper and copper pad both have negligible resistance - good to go
* Wrote voltage output program for arduino mega
* Set up Trello
* Testing if relay is needed - Yiluo
	* Seems like there is no effect, but more testing is needed on the conductive board.
* TODO:
	* Set up the conductive board with copper clip soldered on
	* Start working with tomography visualization
	* Write arduino program to output steady AC current through one pair of electrodes and read voltage at other vertices formed by electrodes


__April 23, 2019__

* Relay is not needed because GND is not necessary in the setup
* For each pair of electrodes that generates current, set one to HIGH voltage and the other one to 0V, and then we can safely read from other electrodes
* When 0V electrode is not needed for purpose of GND, set the pinMode to INPUT, allowing high impedance for the pin
* * We will use Python for tomography visualization, so communication is required between Serial and python


* TODO:
	* Setup the conductive board and measure the resistance density over the board (Frank)
	* Test if the voltage reading is symmetric for different pairs of current-giving electrodes
	* Move the uno code to work on mega (David)
	* Python Serial communication (Yiluo)


__April 24, 2019__

* Painted the conductive board
* The resistance is not very stable, and need to figure out why
* Also the board painting is not uniform, but should not matter if two fixed points have stable resistance reading over time
* 8-electrode model code is working with resistors acting as the surface of the conductive board
* Python serial communication is finished, just need to connect with Arduino and acquire actual data for processing


__April 29, 2019__

* Define some terminologies (based on 8-electros):
	* **1/4 frame** : one pair provides voltage and the rest of them measure.
	* **full frame** : finish iterating 4 electro-pairs and measure the corresponding voltages at each 1/4 frame. At this stage, we can generate our first image.
	* **take turn** : switch from one electros to another
	* **full turns** : go through all electros and finally come back to it self

* General plan:
	* For a 1/4 frame, we take measurements from 6-electros and record them with another two stub data(0V and 5V). 
	* We take measurements on 1/4 frame repeatedly 40 times. It will take arduino (analogread() takes 1/10000s) 0.096s to get all the data.

* To do list:
	* Communication speed between python and arduino is not sure yet; create visualization of voltage on each node. (Yiluo)
	* Get robots setup. (Frank)
	* Build high-pass filter and low pass filter to generate High Frequency AC current.

