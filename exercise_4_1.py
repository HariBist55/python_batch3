# Get user input
user_input = input("Enter a string: ")

# Calculate the length of the string
length = len(user_input)

# Split the string into words and store in a list
words = user_input.split()

# Calculate the total number of words
word_count = len(words)

# Display the results
print(f"Length of the string: {length} characters")
print(f"Total number of words: {word_count}")
print(f"Words in the string: {words}")
