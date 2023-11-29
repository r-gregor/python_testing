#! /usr/bin/env python3
# FamilyMember class test 20170610
# -*- coding: utf-8 *-*


# class comstruction
class FamilyMember:
    """
The FamilyMember class takes name, age, gender and heigth parameters.
'age' and 'heigth' are to be enterd as digits, the rest of parameters
as strings between "".
    """
    def __init__(self, name, age, gender, heigth):
        self.name = name
        self.age = age
        self.gender = gender
        self.heigth = heigth

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_heigth(self):
        return self.heigth

# instantiating object for ech family member
G = FamilyMember("Gregor Redelonghi", 49, "M", 1.85)
M = FamilyMember("Mark Redelonghi", 18, "M", 1.79)
T = FamilyMember("Tadeja Mali Redelonghi", 47, "F", 1.60)
Z = FamilyMember("Zala Redelonghi", 21, "F", 1.59)
S = FamilyMember("Špela Redelonghi", 9, "F", 1.39)

def show_family():
    """
    Function show_family

    Function loops trough family members and displays theirs properties!
    """
    # Looping trough family member objects to print all their properties
    for FM in G, M, T, Z, S:
        name = FM.get_name()
        age = FM.get_age()
        gen = FM.get_gender()
        hgt = FM.get_heigth()

        fage = str(age) # age as string
        fhgt = str(round(hgt,4)).ljust(4,"0") # heigth in "X.XX" format as string

        if gen == "M":
            prfx = "He"
            prfx2 = prfx
            if int(age) >= 21:
                ggen = "MAN"
            else:
                ggen = "BOY"
        else:
            prfx = "She"
            prfx2 = "Her"
            if int(age) >= 21:
                ggen = "WOMAN"
            else:
                ggen ="GIRL"
        
        print(name + "'s age is " + fage + ". " + prfx + " is a \"" + ggen + "\". And " + prfx2 + "'s heigth is " + fhgt + " m.")

# show_family()
