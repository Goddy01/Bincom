# QUESTION 1
# create a list of colors
colors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']

# create a dictionary that maps colors to numerical values
color_values = {
    'GREEN': 1,
    'YELLOW': 2,
    'BROWN': 3,
    'BLUE': 4,
    'PINK': 5,
    'ORANGE': 6,
    'CREAM': 7,
    'RED': 8,
    'WHITE': 9,
    'BLACK': 10
}

# initialize a total variable
total = 0

# iterate through the colors and add the corresponding value to the total
for color in colors:
    total += color_values[color]

# divide the total by the number of colors to get the mean
mean = total / len(colors)

# print the mean
print(mean)



# QUESTION 2
# Define the colors worn each day of the week
monday_colors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
tuesday_colors = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']
wednesday_colors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
thursday_colors = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
friday_colors = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

# Define a dictionary to map the colors to numerical values
color_values = {
    'GREEN': 1,
    'YELLOW': 2,
    'BROWN': 3,
    'BLUE': 4,
    'PINK': 5,
    'ORANGE': 6,
    'CREAM': 7,
    'RED': 8,
    'WHITE': 9
}

# Initialize a dictionary to store the count of each color
color_counts = {}

# Loop through the colors worn each day of the week and add to the count for each color
for day_colors in [monday_colors, tuesday_colors, wednesday_colors, thursday_colors, friday_colors]:
    for color in day_colors:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

# Find the color with the highest count
most_worn_color = max(color_counts, key=color_counts.get)

print(f'The most worn color throughout the week is {most_worn_color}')



# QUESTION 3
colors = [
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'
]

# Define a dictionary to map the colors to numerical values
color_values = {
    'GREEN': 1,
    'YELLOW': 2,
    'BROWN': 3,
    'BLUE': 4,
    'PINK': 5,
    'ORANGE': 6,
    'CREAM': 7,
    'RED': 8,
    'WHITE': 9
}

# Create a list of the numerical values of the colors
values = [color_values[color] for color in colors]

# Sort the values in ascending order
values = sorted(values)

# Calculate the median value
if len(values) % 2 == 0:
    # If the number of values is even, the median is the average of the two middle values
    median_color = (values[len(values) // 2 - 1] + values[len(values) // 2]) / 2
else:
    # If the number of values is odd, the median is the middle value
    median_color = values[len(values) // 2]

print(f'The median of the colors is {median_color:.2f}')



# QUESTION 4
colors = [
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'
]

# Define a dictionary to map the colors to numerical values
color_values = {
    'GREEN': 1,
    'YELLOW': 2,
    'BROWN': 3,
    'BLUE': 4,
    'PINK': 5,
    'ORANGE': 6,
    'CREAM': 7,
    'RED': 8,
    'WHITE': 9
}

# Create a list of the numerical values of the colors
values = [color_values[color] for color in colors]

# Calculate the mean of the values
mean = sum(values) / len(values)

# Calculate the variance
variance = sum((value - mean)**2 for value in values) / (len(values) - 1)

print(f'The variance of the colors is {variance:.2f}')



# QUESTION 5
colors = [
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'
]

# Define a dictionary to map the colors to numerical values
color_values = {
    'GREEN': 1,
    'YELLOW': 2,
    'BROWN': 3,
    'BLUE': 4,
    'PINK': 5,
    'ORANGE': 6,
    'CREAM': 7,
    'RED': 8,
    'WHITE': 9
}

# Count the number of red colors
red_count = 0
for color in colors:
    if color == 'RED':
        red_count += 1

# Calculate the probability that a randomly chosen color is red
probability = red_count / len(colors)

print(f'The probability that a randomly chosen color is red is {probability:.2f}')



# QUESTION 6
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='user',
    password='password',
    database='database'
)

# Create a cursor to execute queries
cursor = conn.cursor()

# Define the colors and their frequencies
colors = {
    'GREEN': 2,
    'YELLOW': 1,
    'BROWN': 1,
    'BLUE': 4,
    'PINK': 1,
    'ORANGE': 2,
    'CREAM': 1,
    'RED': 1,
    'WHITE': 3
}

# Iterate through the colors and insert them into the database
for color, frequency in colors.items():
    cursor.execute(
        'INSERT INTO colors (color, frequency) VALUES (%s, %s)',
        (color, frequency)
    )

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()



# QUESTION 7
def search(numbers, target):
    # Base case: if the list is empty, return False
    if not numbers:
        return False
    # If the target is the first element of the list, return True
    elif numbers[0] == target:
        return True
    # Otherwise, call the function recursively on the rest of the list
    else:
        return search(numbers[1:], target)

# Test the function
numbers = [1, 2, 3, 4, 5]
target = 3
result = search(numbers, target)
print(result)  # Output: True



# QUESTION 8
import random

# Generate a random 4-digit number of 0s and 1s
binary_number = ''.join(str(random.randint(0, 1)) for _ in range(4))
print(f'Generated binary number: {binary_number}')

# Convert the binary number to base 10
base_10_number = int(binary_number, 2)
print(f'Converted base 10 number: {base_10_number}')



# QUESTION 9
# Initialize the first two numbers in the sequence
a, b = 0, 1

# Initialize a variable to store the sum
sum = 0

# Loop through the first 50 numbers in the sequence
for i in range(50):
    # Add the current number to the sum
    sum += a
    # Update the values of a and b
    a, b = b, a + b

print(f'The sum of the first 50 numbers in the Fibonacci sequence is {sum}')