# Crazyflie 2.1 Brushless

### Install the CFClient UI
1. Navigate to the [Installation Instructions](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/installation/install/) page
2. Run python3 -m pip install cfclient
3. When you have installed the client according to the instructions below, you can run the clients with the following commands:
    * cfclient
    * cfheadless
    * cfloader
    * cfzmq

### Update your Crazyradio firmware
1. Follow the [following instructions](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyradio-2-0/)

### Update your Flow Deck firmware
1. IMPORTANT NOTE - the Crazyflie 2.1 Brushless firmware is "cf21bl" NOT "cf2". You will brick your drone and have to restart in Recovery Mode if you flash the cf2 firmware.

### Issue with Firmware Flashing
1. See here for [Recovery Mode](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/userguides/recovery-mode/)

### Light Indicators
* From the crazyflie [light indicators page](https://crazyflie-docs.readthedocs.io/en/latest/getting_started/light_indicators.html)

#### Drone Lights
* 2 blue = drone is running correctly
* 1 red + 1 orange = the drone has experienced an error
* 1 red light (rapidly flashing) = the lower the drone battery, the faster the flashing 
* 1 red light (not flashing) = low battery
* 1 green light (flashing) = the drone is receiving commands
* 1 green/orange light = drone sending info
* 2 blues (flashing) = the drone is in “flash firmware” mode
* 1 red light repeatedly blinking five short red pulses with a longer pause between groups = self test fails. 
    * It could be because of an assert fail(runtime error, i.e. divided by 0), which would be printed in the console. 
    * Restart the Crazyflie if that is the case (and debug).
    * Note: If one Crazyflie does not connect for no apparent reason, then restart it. It may be stuck in an internal loop.

#### Crazyradio Lights
* 1 green light = the radio is transmitting and receiving data correctly
* 1 red light = the radio is transmitting data but is not receiving anything
* 1 red + 1 green = drone is flying

### CrazySim
* [CrazySim: A Software-in-the-Loop Simulator for the Crazyflie Nano Quadrotor](https://github.com/gtfactslab/CrazySim)
* [CrazySim - Bitcraze Article](https://www.bitcraze.io/2024/04/crazysim-a-software-in-the-loop-simulator-for-the-crazyflie/)
