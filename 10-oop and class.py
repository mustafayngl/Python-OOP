# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:50:13 2022

@author: 211015033
"""

#object orianted programming
#class : a set or category of things having some attribute in common
#OOP : is a method of stracting a program by bundling related properties an behaviors(fnc or method) into individual objects.
#define a class ,create a object
#procedural programming
"""
kirk = ["James,Kirk",44,"Captain",2002,2020]
spock = ["Spock",45,"ScienceOfficer",2002,2008]
mccoy = ["LeonardMccoy",50,"ChiefMedicalOfficer",2010]

class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self,sound):
        return f"{self.name} says {sound}"
    def description(self):
        return f"{self.name} is {self.age} years old"
    def walk(self):
        return "I am walking...."
        

buddy = Dog("Buddy",2)
miles = Dog("Miles",4)
buddy.name = "Fırfır"
print(buddy.name)
print(buddy.species)
print(buddy.speak("Hav hav"))
print(miles.description())
print(miles.walk())
"""

class Cars:
    def __init__(self,brand,model,year,cartype,fueltype):
        self.brand = brand
        self.model = model
        self.year = year
        self.cartype = cartype
        self.fueltype = fueltype
    def color(self):
        return "U can choose between black or white color"
    def fuelburn(self):
        return f"{self.brand} {self.model} can travel 23km/L with {self.fueltype}"
    def carage(self):
        return f"{self.brand} {self.model} cars age is {2022-self.year} years old"
    def maintance(self):
        return f"{self.brand} {self.model} needs periodic maintance once in a year"

porsche = Cars("porsche","taycan",2019,"casual","electricity")
porsche = Cars("porsche","taycan",2015,"casual","electricity")
porsche = Cars("porsche","taycan",2013,"casual","electricity")
porsche = Cars("porsche","taycan",2011,"casual","electricity")
print(porsche.brand)
print(porsche.model)
print(porsche.carage())
print(porsche.maintance())
print(porsche.color())
