# Crazyflie 2.1 Brushless

Welcome to the **Crazyflie 2.1 Brushless** repository!  
This repo contains setup notes, troubleshooting tips, and resources for working with the brushless Crazyflie 2.1 nano quadcopter.  

---

## Authors
* Duncan Calvert
* Zachary Farahany
* Steve Barry

---

## Contributing
Feel free to fork this repository, submit pull requests, or open issues with suggestions and improvements. If you find this helpful, consider giving it a ⭐ to support the project!

---

## Installation

### Install the CFClient UI
1. Navigate to the [Installation Instructions](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/installation/install/) page.  
2. Run:
   ```bash
   python3 -m pip install cfclient
3. Once installed, you can run the clients with:
   * cfclient
   * cfheadless
   * cfloader
   * cfzmq
  
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

---

## Light Indicators
From the crazyflie [light indicators page](https://crazyflie-docs.readthedocs.io/en/latest/getting_started/light_indicators.html)

### Drone Lights
* 🔵🔵 Two blue = Running correctly
* 🔴🟠 One red + one orange = Error
* 🔴 (fast flashing) = Battery critically low (flash speed reflects level)
* 🔴🔵🔵 (steady) = Low battery
* 🟢🔵🔵 (flashing) = Receiving commands
* 🟢🟠 Green + orange = Drone is sending info
* 🔵🔵 (flashing) = Firmware flashing mode
* 🔴 (5 short pulses + pause) = Self-test failed
   * It could be because of an assert fail(runtime error, i.e. divided by 0), which would be printed in the console. 
   * Restart the Crazyflie if that is the case (and debug).
   * Note: If one Crazyflie does not connect for no apparent reason, then restart it. It may be stuck in an internal loop.

### Crazyradio Lights
* 🟢 Green = Transmitting and receiving correctly
* 🔴 Red = Transmitting but not receiving
* 🔴🟢 Red + Green = Drone is flying

---

### Simulation Environments
CrazySim
* [CrazySim: A Software-in-the-Loop Simulator for the Crazyflie Nano Quadrotor](https://github.com/gtfactslab/CrazySim)
* [CrazySim - Bitcraze Article](https://www.bitcraze.io/2024/04/crazysim-a-software-in-the-loop-simulator-for-the-crazyflie/)
