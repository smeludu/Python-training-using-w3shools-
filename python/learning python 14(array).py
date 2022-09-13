cars = ["Ford", "volvo", "BMW"]
x = cars[0]#prints one of the vaue in each set.
print(x)#prints the value 'Ford' because the array set start with 0


cars = ["Ford", "volvo", "BMW"]
cars[0] = "Toyota" #changes one of the value in array car
print(cars)#prints the value 'Toyota' because the array set starting with 0 has been upddated 


#printing the length of an array 
cars = ["Ford", "volvo", "BMW"]
x = len(cars)
print(x)


#looping arrays 
cars = ["Ford", "volvo", "BMW"]
for x in cars:
    print (x)


#adding element to array
cars = ["Ford", "volvo", "BMW"]
cars.append("Honda") #adds the value to the back as in 0, 1, '2'
print(cars)

#removing from the array 
cars = ["Ford", "volvo", "BMW"]
cars.pop(1) #pops out the "volvo"
print(cars)

#the difference between popping and removing a value from an array is that pop uses the value is number and remove takes out the name of the value you want to remove 
cars = ["Ford", "volvo", "BMW"]
cars.remove("volvo") #removes the "volvo"
print(cars)

#methods 
# clear() #removes everything in the element 
# copy() #returns a copy of the list 
# count() #can also act as length 
# insert() #inserts an element/value 
# reverse() #reverse the order of the list 
# sort() #sorting the list, can also do it in ascending or decending order 