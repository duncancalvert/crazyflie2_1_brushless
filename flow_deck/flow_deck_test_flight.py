"""
This script shows a simple scripted flight path using the MotionCommander class.

Simple example that connects to the crazyflie at `URI` and runs a
sequence. Change the URI variable to your Crazyflie configuration.
"""
import logging
import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M/E7E7E7E7E8'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI) as scf:
        # Arm the Crazyflie
        scf.cf.platform.send_arming_request(True)
        time.sleep(1.0)

        # We take off when the commander is created
        with MotionCommander(scf, default_height=1) as mc:
            print('Taking off!')
            time.sleep(1)
            
            print('Moving up 0.3m')
            mc.up(0.3)
            # Wait a bit
            time.sleep(1)

            # We can move in all directions
            print('Moving forward 1m')
            mc.forward(2)
            # Wait a bit
            time.sleep(1)
            
            mc.circle_left(velocity=0.2, angle_degrees=180.0)

            # Move forward
            print('Moving forward 0.5m')
            mc.forward(1)
            
            

            # We land when the MotionCommander goes out of scope
            print('Landing!')
