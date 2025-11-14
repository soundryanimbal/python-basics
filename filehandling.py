# Basic file handling example

# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, this is a sample text file.\n")
    f.write("Python file handling is easy!")

# Reading the file
with open("example.txt", "r") as f:
    content = f.read()
    print("File Contents:")
    print(content)
