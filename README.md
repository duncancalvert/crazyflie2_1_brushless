# Crazyflie 2.1 Brushless

Welcome to the **Crazyflie 2.1 Brushless** repository! This repo contains setup notes, troubleshooting tips, and resources for working with the brushless Crazyflie 2.1 nano quadcopter.  

<br>

<div align="center">
<img src="media/crazyflie_drone_top_view.png" alt="A top-down view of the Crazyflie brushless 2.1 drone showing rotor directions" width="60%"/>
</div>

<br>


## Authors
* [Duncan Calvert](https://github.com/duncancalvert)
* [Zachary Farahany](https://github.com/zachfara)
* [Steve Barry](https://github.com/steviebuchicago)


## Contributing
Feel free to fork this repository, submit pull requests, or open issues with suggestions and improvements. If you find this helpful, consider giving it a ⭐ to support the project!


## Installation

### 1. Install the CFClient Globally
1. Navigate to the [Installation Instructions](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/installation/install/) page.  
2. Run:
   ```bash
   python3 -m pip install cfclient

3. Once installed, you can run the clients with:
   ```bash
   * cfclient
   * cfheadless
   * cfloader
   * cfzmq
### 2. Install uv Package Manager
* Run:
   ```bash
   pip install uv

### 3. Create a Virtual Env and Install All Dependecies
* To create a uv virtual env, run: 
   ```bash
   uv venv

* Run:
   ```bash
   uv pip install -r requirements.txt


### 4. Update the Crazyradio 2.0 Firmware
* Follow the [following instructions](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyradio-2-0/)
* Note, you will need to update the Crazyradio firmware before updating any deck firmware

<br>

<div align="center">
<img src="media/crazyradio_2_0.jpg" alt="The Crazyradio 2.0" width="40%"/>
</div>

<br>

### 5. Expansion Decks & Deck Firmware Updates

#### Issues with Crazyflie Firmware Flashing
* <ins>Crazyflie 2.1 Brushless Name</ins>: the firmware is "cf21bl" NOT "cf2". You will brick your drone and have to restart in Recovery Mode if you flash the "cf2" firmware.
* 🔵🔵 Two blue (not flashing) = issues with firmware (generally easy to recover with the below steps)
* 🔵 One blue (not flashing) = issues with nRF51 chip (harder to recover, requires specialized cables)


#### Booting Into Recovery Mode & Reflashing Firmware
* If you have issues with firmware flashing, you'll have to boot into [recovery mode](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/userguides/recovery-mode/) and reflash the correct software
* To boot into recovery mode and reflash the drone, do the following:
   * Disconnect the drone from all power sources (usb and battery)
   * Hold down the power button for 3 seconds and reconnect either of the power sources
   * The two blue lights should alternatively flash, signaling that you're in recovery mode
   * Plug in your crazyradio
   * Boot the cfclient by typing "cfclient" in your computer's terminal
   * On the top navigation, click "Connect" -> "Bootloader"
   * In the popup window tab over to "Cold boot (recovery)
   * Choose "Initate bootloader, cold boot". You should see a message letting you know that the drone has successfully entered bootloader mode
   * Load new firmware using either the file loader or autoloader option and click "Program"
   * Your drone should now be fixed

#### Flow Deck
The Flow deck lets the drone understand what direction it is moving, hover, and abstracts away the need to write low-level stabilization controls. Importantly, unlike the Lighthouse deck, it does not include a global positioning system, meaning the longer the drone flies, the larger the possible X, Y, Z error rate.
* For installation and flashing instructions, see [Getting Started with the Flow Deck](https://www.bitcraze.io/documentation/tutorials/getting-started-with-flow-deck/)

<br>

<div align="center">
<img src="media/crazyflie_flow_deck.jpg" alt="The Crazyflie Flow Deck" width="40%"/>
</div>

<br>


#### AI Deck
The AI deck enables WiFi communication as well as onboard neural network processing using the power-efficient GAP8 board. The AI deck also comes with a connected black and white camera with the option of upgrading to a color camera.
* For installation and flashing instructions, see [Getting Started with the AI Deck](https://www.bitcraze.io/documentation/tutorials/getting-started-with-aideck/)

<br>

<div align="center">
<img src="media/crazyflie_ai_deck.jpg" alt="The Crazyflie AI Deck" width="40%"/>
</div>

<br>


#### Lighthouse Deck
The Lighthouse positioning system uses a combination of the ground-mounted SteamVR Base stations and the drone-mounted Lighthouse deck. This allows the Crazyflie to estimate its X, Y and Z positions in a global coordinate system with a high degree of accuracy.
* For installationa and setup instructions see [Getting started with the Lighthouse system](https://www.bitcraze.io/documentation/tutorials/getting-started-with-lighthouse/)

<br>

<div align="center">
<img src="media/crazyflie_lighthouse_deck.jpg" alt="The Crazyflie Lighthouse Deck" width="40%"/>
</div>

<br>

<div align="center">
<img src="media/crazyflie_lighthouse_base_stations.png" alt="The Crazyflie Lighthouse Positioning System" width="60%"/>
</div>

<br>


### 6. Create a .env File in Your Repo
* Add your radio URI to it. For Crazyflie 2.1 your radio can be found via the cfclient and generally comes in the form of 'radio://0/80/2M/E7E7E7E7E8'
* Example:
   ```bash
   RADIO_URI='radio://0/80/2M/E7E7E7E7E8'


## Drone Light Indicators
From the crazyflie [light indicators page](https://crazyflie-docs.readthedocs.io/en/latest/getting_started/light_indicators.html)
* 🔵 One blue (not flashing) = issues with nRF51 chip
* 🔵🔵 Two blue (not flashing) = issues with firmware
* 🔵🔵 (alternating flashing) = Recovery mode
* 🔴🟠 One red + one orange = Error
* 🔴🔵🔵 (red flashing steady) = Low battery
* 🔴🔵🔵 (red flashing fast) = Battery critically low
* 🟢🔵🔵 (flashing) = Receiving commands
* 🟢🟠 Green + orange = Drone is sending info
* 🔴 (5 short pulses + pause) = Self-test failed
   * It could be because of an assert fail(runtime error, i.e. divided by 0), which would be printed in the console. 
   * Restart the Crazyflie if that is the case (and debug).
   * Note: If one Crazyflie does not connect for no apparent reason, then restart it. It may be stuck in an internal loop.

## Crazyradio Light Indicators
* 🟢 Green = Transmitting and receiving correctly
* 🔴 Red = Transmitting but not receiving
* 🔴🟢 Red + Green = Drone is flying


## Crazyflie Components & Chips
* [STM32F405 ARM chip (Main Crazyflie processing)](https://www.st.com/en/microcontrollers-microprocessors/stm32f405-415.html): A Cortex-M4 processor running at 168 MHz, with 192kb of SRAM and 1Mb of flash memory.
   * The chip is located at the center bottom of the Crazyflie
   * The two chips communicate using the syslink protocol, with the STM32F405 acting as the master and the nRF51822 as the slave
* [nRF51822 Chip (Radio and Power Management)](https://en.wikipedia.org/wiki/NRF51_series): part of the nRF51 series of System-on-Chips (SoC) from Nordic Semiconductor. 
   * SoCs are integrated circuit that combines a processor (MCU), memory, and wireless communication peripherals (like Wi-Fi or Bluetooth) onto a single chip. 
   * The nRF51822 hass a Cortex-M0 processor running at 32 MHz, with 16kb of SRAM and 128kb of flash memory. 
* <ins>White battery connector cord</ins>: JST-PH 2.0 (also called “Micro JST”) connector is used to plug in the single-cell LiPo battery that powers the Crazyflie.
* <ins>Expansion deck connector</ins>: a 2×10 2.54 mm (0.1”) male pin connector
   * Purpose: Provides power, I²C, SPI, UART, GPIO, and other signals from the main MCU
   * Used for:
      * Flow Deck (optical flow + distance sensor)
      * Lighthouse Deck (for SteamVR tracking)
      * AI Deck (camera + ESP32)
      * Multi-ranger Deck, Loco positioning, etc.
* SWD (Serial Wire Debug) / UART connector: the white 6-pin connector on the bottom of the Crazyflie. 
   * Used for low-level programming and debugging of the STM32 microcontroller with a debugger such as the ST-Link V2 or J-Link
   * The 6-pin white port on the Crazyflie 2.1 uses a JST-SH 1.0 mm pitch connector, not the more common 1.25 mm (Molex PicoBlade) or 2.54 mm header types.

### Reference Materials
* [All Crazyflie GitHub Repositories](https://www.bitcraze.io/documentation/repository/)
