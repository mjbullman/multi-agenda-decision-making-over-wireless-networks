#!/bin/bash
#				 Insight Center for Data Analytics
#					   University College Cork
#
#         Ad-hoc networking setup code 3
#
# @author - Martin Bullman
# @since - 03/07/2014

ip link set wlan0 down
iwconfig wlan0 mode ad-hoc
iwconfig wlan0 channel 4
iwconfig wlan0 essid 'GalileoAD-HOC'
iwconfig wlan0 ap AA:BB:CC:DD:EE:FF
iwconfig wlan0 key 1234567890
ip link set wlan0 up
ip addr add 192.168.1.223/24 dev wlan0
