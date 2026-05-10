import ipinfo
import psutil
import requests
import socket
import time

class IPDetails:
    def __init__(self, API_KEY):
        try:
            handler = ipinfo.getHandler(API_KEY)
            details = handler.getDetails()
        except ipinfo.error.APIError:
            raise Exception("Your ipinfo.io API Key is invalid.")            

        self.__hostname = socket.gethostname()
        self.__ipLocal = socket.gethostbyname(self.__hostname)
        self.__ipPublic = details.ip
        self.__location = (details.city + ", " + details.region)
        self.__ISP = (details.org)

    def getHostname(self):
        return self.__hostname

    def getLocalIP(self):
        return self.__ipLocal

    def getPublicIP(self):
        return self.__ipPublic

    def getLocation(self):
        return self.__location

    def getISP(self):
        return self.__ISP

    def getTransferRates(self, previousStats=None, currentStats=None, interval=1):
        if previousStats is None or currentStats is None:
            before = psutil.net_io_counters()
            time.sleep(interval)
            after = psutil.net_io_counters()
        
        else:
            before = previousStats
            after = currentStats

        upSpeed = (after.bytes_sent - before.bytes_sent) / 1024 / interval
        downSpeed = (after.bytes_recv - before.bytes_recv) / 1024 / interval

        return upSpeed, downSpeed

if __name__ == '__main__':
    details = IPDetails()

    print("You're running: " + details.getHostname() + " @ " + details.getLocalIP())
    print("Public ip: " + details.getPublicIP())
    print("Location: " + details.getLocation())
    print("ISP: " + details.getISP())

    while True:
        up, down = details.getTransferRates()
        print(f"UPLOAD: {up:>8.2f} KB/s | DOWNLOAD : {down:>8.2f} KB/s")
