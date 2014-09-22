buffering_timer
===============

This is a tool for calculating the worst-case delay of a given net in VLSI chips. The worst-delay is printed after the tool is run.

This tool is only tested on a 32-bit Ubuntu (14.04) machine.

How to use this tool?

Go to the root directory and run this. A delay.txt file would be generated. It contains the worst case delay corresponding to each unit wire resistance/capacitance setting.

```bash
python main.py <buffering solution file> <buffer library file> <net file> <unit rc file>
```

Example:

```bash
python main.py buffersolution_net0.txt library.cobalt 0.net cnt_res_cap_5000.txt
```
