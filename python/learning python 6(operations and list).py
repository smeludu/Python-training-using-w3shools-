#Arithmetic operatior
print (10+5)  #addition 


x = 21
y = 7
print (x+y) #addition
print (x-y) #subtraction
print (x*y) #multplication
print (x/y) #division
print (x%y) #modulus: y mod x = ?
print (x**y) #exponentiation
print (x//y) #floor division: after the division then you round to the nearest whole number 


# Assignment operatior and so many more check https://www.w3schools.com/python_operator.asp


#listing 
thislist = ["apple", "banana", "cherry"]
print(thislist)

#allows dupicate values 
thislist = ["apple", "banana", "cherry" "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"] 
print(len(thislist))#the length of the list 
print(type(thislist))#the type of the list 

list1 = ["apple", "banana", "cherry"] #a string list 
list2 = [1, 5, 7, 9, 3] #an integer list
list3 = ["True", "False", "False"] #a boolean list 
list4 = ["abc", 34, True, 40, "male"] #a list with strings, integers and boolean 


print(list1)
print(list2)
print(list3)
print(list4)


#Accessing list 
thislist = ["apple", "banana", "cherry"] 
print(thislist[1])
print(thislist[-1])
print(thislist[2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 
print(thislist[:4]) 
print(thislist[2:]) 
print(thislist[-4:-1]) 

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print ("Yes, 'apple' is in the fruits list")
    

#changing the item value
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #changing 1 through 3
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #changing 1 through 2 
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = [ "watermelon"] #changing 1 through 3
print(thislist)



#inserting item 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.insert(2,"watermelon")
print(thislist)

#adding item 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.append("orange")
print(thislist)


#extending list 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#removing item from list 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#removing specific index from list you can use pop method or del keyword 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#del keyword to del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

del thislist #deleting the entire list but it will cause an error message but clear method doesn't give error message
# commenting "print(thislist)" because it will create an error message"
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Loop list 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(thislist) # line 124 and line 125 are the same but the difference is printing x because of list comprehension  and it then prints as a index list 
 [print(x) for x in thislist]
 
 
 
for i in range(len(thislist)): #prints each value in the list and ends up printing in rows i think
 print(thislist[i])#loop through the index number 
 
#while loop list 
thisist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
 print(thislist[i])
 i = i + 1
 
 
 #listcomprehension 
 
 #not listcomprehension 
 fruits = ["apple", "banana", "cherry", "Kiwi", "mango"]
 newlist = []
 for x in fruits:
     if "a" in x:
         newlist.append(x) #takes the value that has a in fruits and insert them in newlist
    
    
print(newlist)

#list comprhension 
#the difference is you can do all of them in one line code 
fruits = ["apple", "banana", "cherry", "Kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] # the syntax is [newlist = expression for item in iterable if condition == true]
print(newlist)


newlist = [x for x in fruits ] # without an if statment it prints all the value in fruits into newlist 
print(newlist)

#print the changed value from fruits into newlist 
fruits = ["apple", "banana", "cherry", "Kiwi", "mango"]
newlist =[ "hello" for x in fruits ] 
print(newlist)



#returning orange instead of banana using the comprehend list 
fruits = ["apple", "banana", "cherry", "Kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


#sorting list 
thislist = ["orange", "mango", "Kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["100", "50", "65", "82", "23"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "Kiwi", "pineapple", "banana"]#desceding list
thislist.sort(reverse = True)
print(thislist)

thislist = [200, 100, 50, 65, 82, 23] #desceding list 
thislist.sort(reverse = True) # you can reverse this way or thislist.sort(reverse = True) or thislist.reverse() function 
print(thislist)


#not sure i fully commprehend this but let see what it prints 
def myfunc(n):
    return abs (n-50)

thislist = thislist = [200, 100, 50, 65, 82, 23] #prints the lowest value in the list first using functions 
thislist.sort(key = myfunc)
print(thislist)

#i think i understand now but we shall see, stay locked in and opened minded 

#sorting lower case and upper case 
#when we use the sort () function it always prints the upper case first and then lower case 
#to print the lower case first we use str.lower

#upper case first using the regular sort function 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#printing lowercase first 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#copying list - two ways to copy list 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#or 
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) #list () method is a built in method of copying list
print(mylist)

#previous we joined a list by using a method extending now we will join by using operation sign + and using the append method 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x) #remember we have used this method previously to add a value to a list
print(list1)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2) #remember we have used this method previously to add a value to a list
print(list1)