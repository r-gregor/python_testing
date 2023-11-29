#! /usr/bin/env python3
# -*- coding: utf8 -*-

class podatki:
    def __init__(self, nm, lnm, addr, twn, cntr, ins_d, ins_t, eml_1, eml_2, cd, upd_d):
        self.name = nm
        self.lname = lnm
        self.addr = addr
        self.twn = twn
        self.cntr = cntr
        self.ins_d = ins_d
        self.ins_t = ins_t
        self.eml_1 = eml_1
        self.eml_2 = eml_2
        self.cd = cd
        self.upd_d = upd_d

T1 = podatki('Gregor','Redelonghi','Valvasorjeva ulica 5','1000 Ljubljana','Slovenija',20171024,203300,'gredelonghi@gmail.com',None,0,None)
T2 = podatki('Tadeja','Mali Redelonghi','Valvasorjeva ulica 5','1000 Ljubljana','slovenija',20171024,203900,'tadeja.malir@gmail.com',None,0,None)
T3 = podatki('Arnold','Schwartzennegger','HauptBauStrasse 452','7856 Wienna','austria',20170625,181800,'arnold.schwartzennegger@gmail.com',None,0,None)

for PSN in T1, T2, T3:
    print("Name: " + PSN.name)
    print("Last name: " + PSN.lname)
    print("e-mail1: " + PSN.eml_1)
    print("-"*80)
