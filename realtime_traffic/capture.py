import pyshark

capture = pyshark.LiveCapture(interface='eth0')  # replace 'eth0' with your network interface

for packet in capture.sniff_continuously(packet_count=10):
    print(packet)
