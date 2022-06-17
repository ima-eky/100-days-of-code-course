# Reading Files

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing to Files
#This method overwrites contents of the file
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# Opening a File that doesn't exit in write mode will create it from scratch

with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.")

#Appending to Files
#This method does not overwrite contents of file
with open("my_file.txt", mode="a") as file:
    file.write("New text.")


