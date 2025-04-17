# This is my own writting code

# Function to read and display the contents of a file
def read_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            data = file.read()
            # Print the content of the file
            print("Your file is: \n", data)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("File not found")
    finally:
        # Close the file (not necessary here since 'with' handles it automatically)
        file.close()

# Function to append text to a file or create a new file if it doesn't exist
def file_handling(new_file_name, new_text):
    try:
        # Open the file in append mode
        with open(new_file_name, 'a') as file:
            # Write the new text to the file
            new_data = file.write(new_text)
            # Print the text that was added to the file
            print("Your new file is: \n", new_text)
    except FileExistsError:
        # Handle the case where the file already exists (not applicable for append mode)
        print("File already exists")
    finally:
        # Close the file (not necessary here since 'with' handles it automatically)
        file.close()

# Main program starts here
print("Welcome to the file handling app")  # Welcome message

# Prompt the user to enter the name of the file to read
file_name = input("File name to read here: ")
# Call the function to read the file
read_file(file_name)

# Prompt the user to enter the text to append to a file
new_text = input("Enter your file changes: ")
# Prompt the user to enter the name of the file to write to
new_file_name = input("Enter your file name: ")
# Call the function to append text to the file
file_handling(new_file_name, new_text)