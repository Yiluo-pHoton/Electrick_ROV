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