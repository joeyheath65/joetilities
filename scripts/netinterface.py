import psutil
import time
import os
import pandas as pd

os.system('clear')

# copy and paste this in the header of each script
print()
print("        ********************************************************************\n"
      "        **                                                                **\n"      
      "        **            W E L C O M E  TO  J O E T I L I T I E S!           **\n"
      "        **                                                                **\n"
      "        **           This Joetility is the Network Usage Checker          **\n"
      "        **                                                                **\n"
      "        ********************************************************************\n")
print()
# since you're forgetful, add this note to each script tellling what it does bruh
print("        ******                --> USAGE  NOTE <--                     ******\n"
      "        * This Joetility will check and print your current network usage.  *\n"
      "        *      The script will run until you stop it with a CTRL-Z         *\n"
      "        * you'll be asked if you want to add a website site to the list!!  *\n")

time.sleep(2)
UPDATE_DELAY = 1 # in seconds

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

# get the network I/O stats from psutil on each network interface
# by setting `pernic` to `True`
io = psutil.net_io_counters(pernic=True)
while True:
    # sleep for `UPDATE_DELAY` seconds
    time.sleep(UPDATE_DELAY)
    # get the network I/O stats again per interface 
    io_2 = psutil.net_io_counters(pernic=True)
    # initialize the data to gather (a list of dicts)
    data = []
    for iface, iface_io in io.items():
        # new - old stats gets us the speed
        upload_speed, download_speed = io_2[iface].bytes_sent - iface_io.bytes_sent, io_2[iface].bytes_recv - iface_io.bytes_recv
        data.append({
            "iface": iface, "Download": get_size(io_2[iface].bytes_recv),
            "Upload": get_size(io_2[iface].bytes_sent),
            "Upload Speed": f"{get_size(upload_speed / UPDATE_DELAY)}/s",
            "Download Speed": f"{get_size(download_speed / UPDATE_DELAY)}/s",
        })
    # update the I/O stats
    io = io_2
    # panda to print stats in a cool tabular style
    df = pd.DataFrame(data)
    # sort values per column
    df.sort_values("Download", inplace=True, ascending=False)
    # clear the screen based on your OS
    os.system("cls") if "nt" in os.name else os.system("clear")
    # print the stats
    print(df.to_string())

    