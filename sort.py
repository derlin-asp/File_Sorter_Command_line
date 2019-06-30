'''
TO DOs/

bug for fake fille paths form text file if theres blank lines

more than one source file?  change to a CSV file?

add unzipping options

#user input on next line?


find elegant exiting command


add support for only adding file names - the file for easier use

print history function

add more error catching
add help funct -  add manual input so no text file copy pasted


make skipping logic take a string instead of an int   if its worth the effort

#catch all thrown errors from imported classes/modules


have a feature for using all other folders for destination folders

need an ignore feature

recursivley do entire disc drive - seedbox
'''


from pathlib import *
import string
from contextlib import redirect_stdout
import io





def prRed(skk):
    print("\033[91m {}\033[00m" .format(skk))




with open('text-finder-300079.txt', 'r') as reader:
    list_of_paths = reader.read().splitlines()

dict_of_paths = {}
for i,e in enumerate(list_of_paths):  #proba better way of putting it into a dic in one go
    dict_of_paths.update({i:e})


#def history_save()


#with redirect_stdout(f):
#
f = io.StringIO()
#with redirect_stdout(f):



print(dict_of_paths)

base_dir = Path(list_of_paths[0])


files = [e for e in base_dir.iterdir() if e.is_file()]
print("type skip instead of a number to skip a file")
index = 0
#for loop of all source dest and go thorugh them one at a time  - variable for current source/base?
while(index < len(files)):
    try:
        folder_choice = int(input(f"where do you want to move {files[index]}"))
        if files[index].name == "text-finder-300079.txt":
            prRed("Skipping text-finder-300079.txt file")
            index = index + 1
        elif folder_choice ==  -55:
            prRed("File Skipped")
            index = index + 1
        elif folder_choice == -99:
            print("EXITING")
            #exit(99)
            break
        elif folder_choice in dict_of_paths: #checking if integer inputed is a key in dict
            destin = Path(dict_of_paths[folder_choice] + "/" + files[index].name)

            if destin.exists():
                print(f"FIle exists with name: {files[index].name} in the folder {dict_of_paths[folder_choice]}")
                print("No change made: moving to next file")
                index = index + 1

            if not destin.exists(): #checks if file exists allready
                files[index].replace(destin)
                index = index + 1
                print("File Moved ")

        elif folder_choice not in dict_of_paths:
            print("invalid folder choice: re try")
            #give them a chance to re choose
        else:
            print("Something went wrong, no changes made: retry or exit")
    except PermissionError:
        print("Permission Denied: Win Error 5: Skipping file")
        index = index + 1
    except ValueError:
        print("bad input: only integers plz: retrying same file")
    except NameError:
        print("The number chosen is not mapped to a folder")
        print("Retrying same file: no changes made")

    # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    # print(f'Got stdout: "{f.getvalue()}"')