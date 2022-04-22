import os

"""
The error and warning count's will increase each time the program finds an error or warning.
"""
error_count = 0
warning_count = 0

"""
The error and warning list's will store what each instance of error or warning says. 
"""
error_list = []
warning_list = []


path = input("Enter path to file: ") # get the path to the file from user.
assert os.path.exists(path), "No file found: " + str(path) #if path not found assertionError will tell the user "No file found."


with open(path, "r") as f: #Access the file and sets it to the variable 'f'

    """
    This for loop checks each line in the file for "WARNING -" or "ERROR -" if ether is found it will add to the count and append the information to the appropriate counter and list.  
    """
    for line in f:
        if "WARNING -" in line:
            warning_count += 1
            warning_list.append(line)
        elif "ERROR -" in line:
            error_count += 1
            error_list.append(line)

"""
At this point the program is done with the file and it is closed.
"""
print() #Extra space for reading clarity. 
print("Number of warnings:", warning_count) #display how many warning were found.
warning_s_range = int(input("Enter starting range of warnings: ")) #Gets starting range from user
warning_e_range = int(input("Enter ending range of warnings: "))#Gets ending range from user
print(*warning_list[warning_s_range -1: warning_e_range], sep="\n") #displays the information for warnings in the range chosen by user on separate lines. 
print() #Extra space for reading clarity.

print("Number of errors:", error_count) #display how many errors were found.
error_s_range = int(input("Enter starting range of error: "))#Gets starting range from user
errorg_e_range = int(input("Enter ending range of error: "))#Gets ending range from user
print(*error_list[error_s_range - 1: errorg_e_range], sep="\n")
print() #Extra space for reading clarity.


print(input("Press enter to close.")) #Keeps file open until user presses enter to close file.