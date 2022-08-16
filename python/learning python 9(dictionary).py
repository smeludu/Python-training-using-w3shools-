thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
     
}

print(thisdict)
#compared to other methods of storing data dictionary is ordered, changeabble and does not allow duplicate. Dictioanry stores the data values with their pairs.
#printing an item from the list 
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
     
}

print(thisdict["brand"])

#duplicate values will override each other 
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print(thisdict)
print(len(thisdict)) #printing the length of the list 

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict)) #printing type of object type()

x = thisdict.keys() #printing the key and not the value
print(x)


#full example of printing the key and not the values, and updating it 
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
} 
x = car.keys()
print (x)
car["color"]= "white"
print (x) #printing the updated value 

#full example of printing the values, and updating it 
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
} 
x = car.values()
print (x)
car["year"]= "2020"
print (x) #printing the updated value 


#printing items in the list and returning them as tuple
#basically both key and value 

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
} 
x = car.items()
print (x)
car["year"]= "2020" #remember this is how to update or change the value of a key 
car.update({"year": 2020}) #this will update the dicitonary
print (x) #printing the updated value 



#checking if key exist 
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
} 
if "model" in car: #this is a loop
    print ("yes, 'model' is one of the keys in the car dictioanry") 
    
    
    
# to delete you can use pop (), popitem () , del or .clear 
#remember it is the same wiht other storage .copy or newname = oldname()


#nested loop for dictinary 

child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3 
    
}

print(myfamily)