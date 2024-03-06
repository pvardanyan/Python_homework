# we input a numeric filename and it searches it in files_homework folder
# if found we read it, otherwise we prompt to input until it's okay (i.e. file found and it's numeric)
#
# then we ask the user if he/she wants to add to that file or to another one.
# checking and handling errors and with opening the file in append mode "a", appending text from a new line.
# P.S. at the end i don't prompt the user until he/she types the valid name.

while True:
    try:
        filename = input("Please Input a NUMERIC FileName: ")        
        if not filename.isdigit(): 
            raise ValueError
        file = open("files_homework/" + filename, "r")
        print(file.read())
        break
    except FileNotFoundError:
        print("Oh no, seems you have a typo. Try again?")
    except ValueError:
        print("Invalid input. Please enter a valid filename.")
file.close()
    
modify = input("Do you want to write to this file or to a new file (add/new) ? ")

if modify == "add":
    file = open("files_homework/" + filename, "a")
    new_text = input("Please Input the content you want to be added: ")
    file.write('\n' + new_text)
    file.close()

elif modify == "new":
    try:
        filename = input("Please Input the FileName: ")
        if not filename.isdigit(): raise ValueError
        file = open("files_homework/" + filename, "a")
        new_text = input("Please Input the content you want to be added: ")
        file.write('\n' + new_text)
    except Exception as e:
        print("Value error accured")
    else:
        print("Writing was done successfully!") 
    finally:
        file.close()
        print(f"File '{filename}' is closed.")       
