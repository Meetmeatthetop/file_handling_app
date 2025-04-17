# AI modification of my code to meet standard practice

def read_file(file_name):
    """
    Reads the content of a file and prints it to the console.
    :param file_name: Name of the file to read.
    """
    try:
        with open(file_name, 'r') as file:  # Open the file in read mode
            data = file.read()  # Read the file content
            print("Your file content is:\n", data)  # Display the content
    except FileNotFoundError:  # Handle case where the file does not exist
        print("Error: File not found. Please check the file name and try again.")

# Function to append text to a file or create a new file if it doesn't exist
def file_handling(file_name, text_to_append):
    """
    Appends text to a file or creates a new file if it doesn't exist.
    :param file_name: Name of the file to write to.
    :param text_to_append: Text to append to the file.
    """
    try:
        with open(file_name, 'a') as file:  # Open the file in append mode
            file.write(text_to_append)  # Write the new text to the file
            print("The following text has been added to the file:\n", text_to_append)
    except Exception as e:  # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Main program execution starts here
print("Welcome to the File Handling App")  # Welcome message

# Prompt the user to enter the name of the file to read
file_to_read = input("Enter the name of the file to read: ")
read_file(file_to_read)  # Call the function to read the file

# Prompt the user to enter the text to append and the file name
text_to_add = input("Enter the text you want to add to the file: ")
file_to_write = input("Enter the name of the file to write to: ")
file_handling(file_to_write, text_to_add)  # Call the function to append text to the file