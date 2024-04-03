
with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("12345\n")
    file.write("Another line with some text and numbers: 9876\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied while accessing the file.")
except Exception as e:
    print("Error occurred while reading the file:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending a new line\n")
        file.write("67890\n")
        file.write("Last line of the file\n")
except Exception as e:
    print("Error occurred while appending to the file:", e)
else:
    print("Data appended successfully.")

# Error Handling with finally block
try:
    # Attempt to open the file for reading again
    with open("my_file.txt", "r") as file:
        print("\nContents of my_file.txt after appending:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied while accessing the file.")
except Exception as e:
    print("Error occurred while reading the file:", e)
finally:
    print("Script execution completed.")
