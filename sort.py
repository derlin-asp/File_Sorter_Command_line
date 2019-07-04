from zipfile import ZipFile
from file_path_organizer import *


#def write_to_file_and_print(temp_string):


def file_should_be_skipped(current_file):
    if current_file in list_of_ignore_files or current_file.suffix in list_of_ignore_file_types:
        temp_string = f"skipping {current_file.name} as requested "
        return True
    elif current_file == "text-finder-300079.txt":
        temp_string2 = "Skipping text-finder-300079.txt file"
        return True
    else:
        return False



def check_destination_folder_choice_is_exit_or_skip(choice):
    if choice == -99:
        temp_string = "EXITING"
        exit(99)
    elif choice == -55:
        temp_string = "File Skipped"
        return True
    else:
        return False


def move_or_extract_file(current_file,destin):
    if destin.exists():
        temp_string = (f"FIle exists with name: {current_file.name} in the folder {destin}")
        temp_string2 =("No change made: moving to next file")

    if not destin.exists():
        if current_file.suffix == ".zip":
            zf = ZipFile(current_file, 'r')
            zf.extractall(destin)
            # check if the file in zip form is there as well
            zf.close()
            temp_string = "File Zipped into destination folder"
        else:
            current_file.replace(destin)
            print(f"File Moved to {destin}" )

def prRed(skk):
    print("\033[91m {}\033[00m" .format(skk))


temp_list = path_text_file_reader()
#make it easier to read later


list_of_source_paths = temp_list[0]
dict_of_destination_paths = temp_list[1]
list_of_ignore_files = temp_list[2]
list_of_ignore_file_types = temp_list[3]


for i in range(len(list_of_source_paths)):
    base_dir = Path(list_of_source_paths[i]) #needs to change when the first one is done
    files = [e for e in base_dir.iterdir() if e.is_file()]

    print("type -55 instead of a number to skip a file")
    print(dict_of_destination_paths)
    index = 0
    # for loop of all source dest and go thorugh them one at a time  - variable for current source/base?
    while (index < len(files)):
        try:

            if file_should_be_skipped(files[index]):
                index = index + 1
                continue


            folder_choice = int(input(f"Move: {files[index]}  -> "))

            if check_destination_folder_choice_is_exit_or_skip(folder_choice):
                index = index + 1
                continue

            elif folder_choice in dict_of_destination_paths:  # checking if integer inputed is a key in dict
                destin = Path(dict_of_destination_paths[folder_choice] + "/" + files[index].name)

                move_or_extract_file(files[index],destin)
                index = index + 1

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