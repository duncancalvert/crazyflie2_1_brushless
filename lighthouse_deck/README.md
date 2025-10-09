# Crazyflie Lighthouse Deck & Positioning System Guide

Welcome to the **Crazyflie 2.1 Brushless Lighthouse Positioning System Guide**! This README contains setup notes, troubleshooting tips, and resources for working with the Lighthouse Deck. 

The Lighthouse positioning system uses a combination of the ground-mounted SteamVR Base stations and the drone-mounted Lighthouse deck. This allows the Crazyflie to estimate its X, Y and Z positions in a global coordinate system with a high degree of accuracy.


<br>


## Installation

### 1. Ensure general Crazyflie dependecies installed
This guide assumes that you have installed all the general dependecies for the Crazyflie. If not already done, please navigate to the [parent README](README.md) in this repository and completed the numbered steps there.

### 2. Flash the Lighthouse Deck firmware
* Remove any other decks from the drone if mounted
* Remove the drone from any usb connection if connected
* Attach the Lighthouse Deck to the drone pins. Ensure that the front of the deck aligns to the front of the drone (to check this, esnure that the arrow on the deck aligns with the front of the drone)
* Power on the drone
* Run "cfclient" in a terminal to start the Crazyflie app
* Connect to the crazyflie via the client
* Chose what option to use for flashing
   * Use the “From release” tab to automatically use an official release. Make sure to select the right platform (cf2 is the Crazyflie 2.x)
   * To manually flash, use the “From file” tab and download the latest [official release file](https://github.com/bitcraze/crazyflie-release/releases). Be sure to upload the .zip file (i.e. don't decompress it). IMPORTANT NOTE - the Crazyflie 2.1 Brushless firmware is "cf21bl" NOT "cf2". You will brick your drone and have to restart in Recovery Mode if you flash the "cf2" firmware.
* After the flashing progress bar completes, ensure that both blue lights are solid and the red light is flashing to check that flashing was successful.

### 3. Prepare the base stations
* Follow the [Configure the base stations channel (mode) steps](https://www.bitcraze.io/documentation/tutorials/getting-started-with-lighthouse/#configure-the-base-stations-channel-mode-) to set each base station ID.

### 4. Set up the base stations in the flight area
* Follow the [Set up the base stations in the flight area section](https://www.bitcraze.io/documentation/tutorials/getting-started-with-lighthouse/#set-up-the-base-stations-in-the-flight-area) of the official crazyflie docs
* Make sure that you have the following conditions in your flight area:
   * The base stations should be about at least 40 centimeters higher than the flight area of the Crazyflie due to the placement of the sensors on the Lighthouse positioning deck .
   * Make sure that there are no mirrors or big large reflective items in the area.
   * Make sure that you do not have direct sunlight.

### 5. Position the drone
* Set the crazyflie drone on the ground in the origin (middle point) of the two base stations.

### 6. Turn the drone on and connect to it via the cfclient
* Follow the usual procedure to connect to the drone within the cfclient software
* If not already done, [configure the Crazyflie 2.x in 2Mbit radio mode](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/userguides/userguide_client/#firmware-configuration). This reduces the risk of WiFi interference with the radio.

### 7. Check the base station system type (one-time)
* In the Lighthouse positioning tab of the cfclient, click "Change system type" and ensure that V2 is selected.
   * NOTE - The system type is stored with the drone so you should only need to do this once.

### 8. Calibrate the drones position
* Make sure that the Crazyflie is receiving the sweep angels of both base stations and has received the calibration data. You'll know that this is successful if the rectangles are green for both "Receiving" and "Calibration" for channels 1 and 2
   * For the calibration data you might need to wait for 20 seconds.

<div align="center">
<img src="media/lighthouse_deck_readme_basestation_status.png" alt="Lighthouse Deck Calibration" width="40%"/>
</div>

### 9. Estimate Geometry
Once you have received the calibration data, it is time to estimate where the base stations are located
* Open up the base station geometry management dialog by pressing ‘Manage Geometry’ in the Lighthouse tab of the cfclient
* In the dialog, press ‘Estimate Geometry’ (not ‘Manage geometry simple’). Please follow the wizard’s instructions for estimating the geometry. The wizard will ask you to move the drone around in various positions to ensure it gets a proper read of its location.
* If the geometry makes sense, press ‘Write to Crazyflie’, or else move your Crazyflie and press ‘Estimate Geometry’ again.
* Once this is done, all Lighthouse deck lights should be green for both channel 1 and 2 and the base stations and drone should show up on the visualization.



## References:
* [Getting started with the Lighthouse system](https://www.bitcraze.io/documentation/tutorials/getting-started-with-lighthouse/)
* [The Lighthouse positioning system](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/functional-areas/lighthouse/)
* [The Lighthouse Positioning Tab](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/userguides/userguide_client/lighthouse_tab/)
* 
