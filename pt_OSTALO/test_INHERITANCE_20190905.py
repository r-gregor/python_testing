#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# BASE = PARENT CLASS
class Family:
    def __init__(self):
        self.lname = "Redelonghi"
        self.addr  = "Valvasorjeva ulica 5, 1000 Ljubljana"

# SIBLING CLASS
class Fmember(Family):
    def __init__(self, name, phone):
        
        # initialize super (parent)
        super(Fmember, self).__init__()
        
        self.name = name
        self.phone = phone
    
        if self.name == "Tadeja":
            self.lname = "Mali Redelonghi"
    
    def getName(self):
        return self.name
    
    def getLname(self):
        return self.lname
    
    def getAddr(self):
        return self.addr
    
    def getPhone(self):
        return self.phone

        
# dict of family objects
rediji = {"gr":Fmember("Gregor", "+386 40885560"),
"zr":Fmember("Zala", "+386 41445505"),
"td":Fmember("Tadeja", "+376 410623097"),
"sr":Fmember("Špela", "+386 707 404"),
"mr":Fmember("Mark", "+386 51454455")}

# func to display members info from all mems in dict
def dispMems(mem):
    print("{0}\n{1}\n{2}\n{3}\n".format(mem.getName(),
                                       mem.getLname(),
                                       mem.getPhone(),
                                       mem.getAddr()
                                       )
    )

for m in rediji:
    dispMems(rediji.get(m))
