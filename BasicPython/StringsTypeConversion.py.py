
 #Strings
# Strings are take extra space why it's take extra space -- 
# every charecter how unique code Ex . A = 65 that wish take extra space 
# you want to se unique code of charecters 
uc = "A"
print(ord(uc)) # output : 65

# you and to check the uniquecode to charecter
uc = 65
print(chr(uc)) # output : A 

# String indexing 
# now you know the string are store to many charecters 
# now qus is can we access the each charecters - yes 
# by the indexing we can access each charecters

# two type of indexing possive and negitive indexing 
# possive indexing start with 0 
# negitive indexing start with -1 
# in indexing space also calculate 
Name = 'Rohan Ka Adda' # 13
# have to access index [] 
print(Name[0]) #output : R 
print(Name[1]) #output : o
print(Name[13]) #output : a 
# negative indexing 
print(Name[-1],Name[0]) #output : a R

# String Slicing 
# slicing means cutting out a slice from string and this is also done uding index values

a = 'Rohan Ka Adda' # 13
# in slice we have 3 steps a[start:stop:step]

print(a[0:6:1]) # Rohan
print(a[:4:1]) # Roh


# Type Conversion 

# we can see the datatypes int(), float(), str(), bool() 
# we can converate the data type of varibales 
# lets see how to convarate data type 

b = 12
b= str(b) # we can converate anything in str
print(b) # 12

c = '12'
c = int(c) # we can converate numaric string only not other character like a,d,e,v,e
print(c) # 12

d = "hello"
d = bool(d) # All String are True  but only 7 value are False like -> False, 0, 0.0, "", [],(),{}
print(d) # True 

# explicit Type conversion - means python automatically converate 

print(2/2) # 1.0 here convarte into float 


