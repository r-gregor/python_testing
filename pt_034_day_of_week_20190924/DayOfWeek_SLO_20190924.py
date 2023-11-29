#!/usr/bin/env python3
# coding: utf-8

def dayOfWeek(currday, offset):
    weekDays = {1:"Ponedeljek", 2:"Torek", 3:"Sreda", 4:"četrtek", 5:"Petek", 6:"Sobota", 7:"Nedelja"}
 
    day = abs(  (currday + offset) % 7  )
    
    # ternary if expression
    day = currday if day == 0 else day
    
    print("Če je danes {}, je čez {} dni {}.".format(weekDays.get(currday), offset, weekDays.get(day)))

dayOfWeek(2, 108)
dayOfWeek(2, 142)
dayOfWeek(7, -8)
dayOfWeek(7, 140)
dayOfWeek(7, -280)
