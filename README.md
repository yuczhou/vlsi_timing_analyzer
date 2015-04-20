buffering_timer
===============

This is a tool for calculating the worst-case delay of a given net in VLSI chips. The worst-delay is printed after the tool is run.

This tool is only tested on a 32-bit Ubuntu (14.04) machine.

How to use this tool?

Go to the root directory and run this. A delay file with user defined name would be generated. It contains the worst case delay corresponding to each unit wire resistance/capacitance setting.

To consider carbon nanotube (CNT) fabrication variations on the CNT wire length, uniformly distributed random adjustments to wire length is implemented. Random numbers corresponding to X and Y coordinate is read from the user specified file.
This feature is turned off by default. To turn it on, change `TEST_MODE` to be `False` in `timer/settings.py`

```bash
python main.py <buffering solution file> <buffer library file> <net file> <unit rc file> <random number file> <output delay file>
```

Example:

```bash
python main.py buffersolution_net0.txt library.cobalt 0.net cnt_res_cap_5000.txt spa_net0.txt delay.txt
```
