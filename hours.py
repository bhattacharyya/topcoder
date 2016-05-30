#!/usr/bin/python

etime = raw_input("Enter time: ")

hours = etime[0:2]
minutes = etime[3:5]

hourHand = int(hours)
minuteHand = int(minutes) / 5

temp = hourHand
hourHand = minuteHand
minuteHand = temp

newHourHand = str(hourHand)
if hourHand < 10:
	newHourHand = "0" + str(hourHand)

if  newHourHand == "00":
	newHourHand = 12

newMinutehand = str(minuteHand * 5)
if (minuteHand * 5) < 10 :
	newMinutehand = "0" + str(minuteHand * 5)

print "\nNew time is : " , newHourHand, ":" , newMinutehand, "\n"
