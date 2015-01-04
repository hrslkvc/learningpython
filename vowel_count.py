vowels = 0
s = input("Enter a string: ")
for i in s:
    if i in "aeiouAEIOU":
        vowels += 1 
print("The string you entered has {} vowels".format(vowels))
