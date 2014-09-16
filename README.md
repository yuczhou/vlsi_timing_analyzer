buffering_timer
===============

This is a tool for calculating the worst-case delay of a given net in VLSI chips. The worst-delay is printed after the tool is run.

This tool is only tested on a 32-bit Ubuntu (14.04) machine.

python main.py <buffering solution file> <buffer library file> <net file>

Example: python main.py buffersolution_net0.txt library.cobalt 0.net
