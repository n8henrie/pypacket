#!/usr/bin/env python

import time
from pypacket.base.listener import Listener
from pypacket.util.colors import Colors

print(Colors.GREEN + """
  ___      ___         _       _
 | _ \_  _| _ \__ _ __| |_____| |_
 |  _/ || |  _/ _` / _| / / -_)  _|
 |_|  \_, |_| \__,_\__|_\_\___|\__|
      |__/
""" + Colors.RESET)

# The main runner.
pypacket_runtime = Listener()

# Handles Control+c interrupts, existing the main loop and threads.
try:
    while True:
        time.sleep(.05)
except KeyboardInterrupt:
    pypacket_runtime.stop()