#!/usr/bin/env python3
# coding: utf-8

def dayOfWeek(currday, offset):
    weekDays = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
 
    day = abs(  (currday + offset) % 7  )
    
    # ternary if expression
    day = currday if day == 0 else day
    
    print("Week day {} days from {} is: {}".format(offset, weekDays.get(currday), weekDays.get(day)))

dayOfWeek(2, 108)
dayOfWeek(2, 142)
dayOfWeek(7, -8)
dayOfWeek(7, 140)
dayOfWeek(7, -142)
dayOfWeek(7, -280)
