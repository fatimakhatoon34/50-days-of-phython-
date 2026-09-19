# Working with Lists in Python
# ------------------------------------------

# Basic setup
fruits = ["apple", "banana", "cherry"]
scores = [10, 5, 20, 15, 5]

# Adding new items
fruits.append("orange")
fruits.insert(1, "blueberry")

# Cleaning up / removing items
fruits.remove("banana")
last_item = fruits.pop()

# Sorting and searching
scores.sort()
scores.reverse()
total_fives = scores.count(5)
blueberry_pos = fruits.index("blueberry")

# Direct modification
fruits[0] = "strawberry"

print("Updated fruits:", fruits)
print("Sorted numbers:", scores)
print("Number of 5s found:", total_fives)
print("Position of blueberry:", blueberry_pos)
print("Removed last item:", last_item)


# Working with Tuples
# ------------------------------------------

# Tuples are fixed once created
point = (10.5, 20.8, 30.1)
colors = ("red", "green", "blue", "green")

# Checking tuple data
green_occurrences = colors.count("green")
blue_pos = colors.index("blue")

# Unpacking values directly into variables
x_pos, y_pos, z_pos = point

print("\nTuple values:", point)
print(f"Unpacked coordinates: x={x_pos}, y={y_pos}, z={z_pos}")
print("Times green appears:", green_occurrences)


# Built-in Utility Functions
# ------------------------------------------

data_points = [4, 8, 15, 16, 23, 42]

# General stats
total_count = len(data_points)
sum_total = sum(data_points)
highest = max(data_points)
lowest = min(data_points)

# Converting formats
as_tuple = tuple(data_points)
colors_as_list = list(colors)

print("\nData summary:")
print("Total items:", total_count)
print("Sum of items:", sum_total)
print("Range:", lowest, "to", highest)
print("Converted list to tuple:", as_tuple)


# Looping & Data Processing
# ------------------------------------------

users = ["alice", "bob", "charlie"]
user_scores = [85, 92, 78]

# Standardize text formatting
formatted_users = [user.upper() for user in users]

# Attach index numbers to list items
numbered_users = list(enumerate(users, start=1))

# Pair up two separate lists together
user_records = list(zip(users, user_scores))

print("\nProcessed lists:")
print("Uppercase users:", formatted_users)
print("Numbered list:", numbered_users)
print("Paired user scores:", user_records)
