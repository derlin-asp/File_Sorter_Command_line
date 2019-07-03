from zipfile import ZipFile

from pathlib import *
import string
from contextlib import redirect_stdout
import io
from file_path_organizer import *




def prRed(skk):
    print("\033[91m {}\033[00m" .format(skk))


temp_list = path_text_file_reader()
#make it easier to read later
list_of_source_paths = temp_list[0]
dict_of_destination_paths = temp_list[1]
list_of_ignore_files = temp_list[2]
list_of_ignore_file_types = temp_list[3]
print(list_of_ignore_file_types)

for i in range(len(list_of_source_paths)):
    base_dir = Path(list_of_source_paths[i]) #needs to change when the first one is done
    files = [e for e in base_dir.iterdir() if e.is_file()]

    print("type -55 instead of a number to skip a file")
    print(dict_of_destination_paths)
    index = 0
    # for loop of all source dest and go thorugh them one at a time  - variable for current source/base?
    while (index < len(files)):
        try:
            current_file = files[index]

            if files[index].name in list_of_ignore_files or files[index].suffix in list_of_ignore_file_types:
                print(f"skipping {files[index].name} as requested ")
                index = index + 1
                continue

            folder_choice = int(input(f"where do you want to move {files[index]}"))

            if files[index].name == "text-finder-300079.txt":
                print("Skipping text-finder-300079.txt file")
                index = index + 1
            elif folder_choice == -55:
                print("File Skipped")
                index = index + 1
            elif folder_choice == -99:
                print("EXITING")
                exit(99)
                break
            elif folder_choice in dict_of_destination_paths:  # checking if integer inputed is a key in dict
                destin = Path(dict_of_destination_paths[folder_choice] + "/" + files[index].name)

                if destin.exists():
                    print(f"FIle exists with name: {files[index].name} in the folder {dict_of_destination_paths[folder_choice]}")
                    print("No change made: moving to next file")
                    index = index + 1

                if not destin.exists():  # checks if file exists allready
                    if files[index].suffix == ".zip":
                        zf = ZipFile(files[index], 'r')
                        zf.extractall(destin)
                        zf.close()
                    else:
                        files[index].replace(destin)
                        index = index + 1
                        print("File Moved ")

            elif folder_choice not in dict_of_destination_paths:
                print("invalid folder choice: re try")
                # give them a chance to re choose
            else:
                print("Something went wrong, no changes made: retry, skip or exit")
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






print("All files moved")
'''
TO DOs/
add progress bar

add suport for using *.file_type so users dont have to write them all out

add unzipping options
    delete original zip files?


#user input on next line? make 


find elegant exiting command/skipping


print history function


add help funct -  add manual input so no text file copy pasted


have a feature for using all other folders for destination folders


an entire drive feature?  duplicate issues?


'''