print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """"Lorem ipsum dolor sit ament, 
consecteur adipiscing elit,
sed do eiusmond tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit ament, 
consecteur adipiscing elit,
sed do eiusmond tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])


for x in "banana":
 print(x)


a = "Hello, World!"
print(len(a))

#checking string
txt = "The best things in life are free!" #if free is in the text print true
print("free" in txt)

txt = "The best thing in life are free!"
print("expensive" not in txt)


#using if fumction to check the string 
txt = "The best things in life are free!"
if "free" in txt: 
    print ("Yes, free is present")
    
txt = "The best things in life are free!"
if "expensive" not in txt: 
    print ("No, expensive is not present")
    
#let's write them slicing strings 
b = "Hello, World!"
print (b[2:5]) # returning a range of characters using slicing syntax 
print (b[:5]) #from the start 
print (b[2:]) # until you get to the end 
print (b[-5:-2]) # starts from the end of the string 


#lets modify strings 
a = "Hello, World!" #upper case
print (a.upper())
print (a.lower())
print(a.replace("H", "J")) #replaces H with J
print(a.split(",")) #returns the string as a lsit "Hello", "World"

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" without space at the beginning and the ended

#string Concatenation
a = "Hello"
b = "World!"
c = a + b 
print (c)


#adding space to String Concatenation 
c = a + " " + b 
print(c)

#formatting strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) 

quality = 3 
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quality, itemno, price))

myorder = "I want {2} dollars for {0} pieces of item {1}." #you can use index numbers to be sure the argument are placed in the correct placeholders. 
print(myorder.format(quality, itemno, price))

#trying escape charater for fun
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#there are string methods for many things espeically true or false questions https://www.w3schools.com/pyhton/python_strings_methods.asp

