# Calculating the Drake equation based on user input

p = int(input("What percentage of stars do you think have planets: "))
n = int(input("How many planets per star do you think can support life?: "))
f = int(input("What percentage do you think actually develop life?: "))
i = int(input("What percentage of those do you think have intelligent life?: "))
c = int(input("What percentage of those do you think can communicate with us?: "))
L = int(input("Number of years you think civilizations last?: "))

# Calculate the result
civilizations = 7 * (p/100) * n * (f/100) * (i/100) * (c/100) * L

# Display result
print()
print("Based on the values you entered ")
print("there are an estimated", round(civilizations), "potentially detectable civilizations in our galaxy")


