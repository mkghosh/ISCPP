#!/usr/bin/env python3

"""
readanalog.py : Read analog data from an Arduino using pyFirmata.

Copyright (C) Simon D. Levy 2016

This file is part of ISCPP.

ISCPP is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
"""

import pyfirmata
from time import time

print("Connecting to Arduino ... ", end="")
board = pyfirmata.Arduino("/dev/ttyACM0")

it = pyfirmata.util.Iterator(board)
it.start()
 
board.analog[0].enable_reporting()

timestart = time() 

while time() - timestart < 10:
    
    print(board.analog[0].read())
     
board.exit()
