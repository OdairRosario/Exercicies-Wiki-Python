"""
Make a program that asks for the size of a download file (in MB) and the speed of an Internet link (in Mbps),
calculate and inform the approximate download time of the file using this link (in minutes).
"""

size = float(input("What is the file size in MB: "))
speed = float(input("What is the speed in Mbps: "))

time = size / speed
print(f"It will take {time/60} seconds")
