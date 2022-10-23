# Create a variable called 'name' that holds a string
name = "Reginald Brenkman"

# Create a variable called 'country' that holds a string
country = "Canadia"

# Create a variable called 'age' that holds an integer
age = 25

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 15

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8.5
print(type(daily_wage))

# Create a variable called 'satisfied' that holds a boolean
satisfied = True

# Print out "Hello <name>!"
print("Hello"  +  name + "!")

# Print out what country the user entered
print("You are from"  +  country +".")

# Print out the user's age
print("You are"   +  str(age) + "years old.")

# With an f-string, print out the daily wage that was calculated
printf("You Make" + {daily_wage} + "per day.")

# With an f-string, print out whether the users were satisfied
printf("You were" + {satisfied} + "with your wage!")
