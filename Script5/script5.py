# Making a function to calculate the area of a triangle based on user input
	
base = int(input("What is the base of your triangle?: "))
height = int(input("What is the height of your triangle?: "))

def area(base, height):
	return base * height / 2
	
area = area(base, height)

print("The area of your triangle is:", area)


