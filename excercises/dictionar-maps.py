import sys

# Initialize an empty dictionary to store the phonebook
phonebook = {}

# Initialize an empty string to store the result
result = ""

# Read all lines from standard input and strip any leading/trailing whitespace
lines = [line.strip() for line in sys.stdin]

# The first line contains the quantity of phonebook entries
qty = int(lines.pop(0))

# Iterate over the remaining lines
for r, line in enumerate(lines):
    if r < qty:
        # Split the line into name and number and add to the phonebook
        name, number = line.split()
        phonebook[name] = number
    else:
        # Check if the name exists in the phonebook and append the result accordingly
        if phonebook.get(line) is None:
            result += 'Not found\n'
        else:
            result += f"{line}={phonebook.get(line)}\n"

# Remove the trailing newline character from the result
result = result.rstrip('\n')

# Print the final result
print(result)