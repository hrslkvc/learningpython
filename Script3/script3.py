s = "Spam"
#Using len function on a string, converting it to a string and concatenating 
print("The word spam has " + str(len(s)) + " letters")

#Printing each letter of the string 
print(s[0], s[1], s[2], s[3])

#spelling it recursively from the beggining
print(s[:1], s[:2], s[:3], s[:4])

#spelling from particular letter onwards
print(s[0:], s[1:], s[2:], s[3:])

#spelling backwards
print(s[-1], s[-2], s[-3], s[-4])

#spelling from particular letter backwards
print(s[-4:],s[:-1], s[:-2], s[:-3])

#extracting a part of a string
print(s[0:4], s[1:3])

#printing the whole string using len()
print(s[0:len(s)])

#concatenating strings
print("So much "+s)

#repeating a string x number of times
print(s*10)

#printing a message if the location of the letter is in the right place
if s.find("a") == 2:
	print("Yay, the location of 'a' in spam is", s.find("a"))
	
#replacing a part of a string
print(s.replace("pa","ca"))
