# ipdetails
Simple middleman module to bridge (parts of) IPInfo API and some frotend application.
Helped me learn partly about api calls.

## About this project
This was made after someone I know AI-generated some code which was: (a) Slow (b) Not working (c) Not functional. This is 1 of 3 repositories I have created that rewrote, fixed, and improved on the AI-generated slop.
Some challenges I faced:
- Using many different libraries. I have never used ipinfo, psutil and socket before. Writing a class that surrounded these three core packages of IP addresses and networks was interesting.
- Writing classes in Python. Python is weird, and I forget a lot with putting "self" in the arguments or before a member variable. It caught me offguard a lot.
- Creating my own module. I researched a bit of how modules are made with an `'__init__.py'` file and what I needed to do.

## Features
- IPDetails class with getters for hostname, local ip, public ip, etc.
- In the above, a getTransferRates getter which calculates the difference transfer rates between two points in time, and returns it in KB/s
- Everything packed a module, easily accessible to be used.

## Requirements
- Python
- Python ipinfo package

## Licence
Copyright © 2026 Jay Rickaby,
Licensed under the MIT License
