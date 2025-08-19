# This script demonstrates file operations in Python including writing, reading, and error handling.

# Opening a file in write mode and writing content to it
with open('example.txt', 'w') as file:
    for _ in range(5):
        content = file.write("This is a line of text.\n")
    print("File created & written successfully.")

# Opening the file in write mode and writing content in uppercase
with open('example.txt', 'w') as file:
    for _ in range(5):
        content = file.write("This is a line of text.\n".upper())
    print("File Altered successfully to uppercase.")

# Reading the file and counting words
with open('example.txt', 'r') as file:
    content = file.read()
    word_count = len(content.split())
    print(f"Word count: {word_count}")

# Opening a new file in write mode and copying content from previous file to it
with open('output.txt', 'w') as file:
    with open('example.txt', 'r') as read_file:
        content = read_file.read()
        file.write(content)
    print("Content copied to output.txt successfully.")

#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
file_name = input("Enter the name of the file to read (please include the extension e.g .pdf): ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")