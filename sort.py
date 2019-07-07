from zipfile import ZipFile
from file_path_organizer import *

#open and append inside the function but truncate and overwirte on each program start
def write_to_file_and_print(temp_string):
    print(temp_string)
    with open('output_of_file_sorter.txt', 'a') as myfile:
        myfile.write(temp_string)
        myfile.write('\n')

# Further file processing goes here

def file_should_be_skipped(current_file):
    '''
    This function reads the skipping portion of the text file.
    Auto skips all files and types indicated by the user in the text file.
    :param current_file:
    :return: True if files is a skipped one: False if not
    '''
    if current_file in list_of_ignore_files or current_file.suffix in list_of_ignore_file_types:
        temp_string = f"skipping {current_file.name} as requested "
        write_to_file_and_print(temp_string)
        return True
    elif current_file == "text-finder-300079.txt":
        temp_string = "Skipping text-finder-300079.txt file"
        write_to_file_and_print(temp_string)
        return True
    else:
        return False



def check_destination_folder_choice_is_exit_or_skip(choice):
    '''
    checks if the integer folder choice indicates if user wants to skip a file or exit the program
    :param choice: an integer from user input
    :return: True if a file should be skipp. If user input indicates exit then program exits
    '''
    if choice == -99:
        temp_string = "EXITING"
        write_to_file_and_print(temp_string)
        exit(99)
    elif choice == -55:
        temp_string = "File Skipped AS CHOSEN VIA INPUT"
        write_to_file_and_print(temp_string)
        return True
    else:
        return False


def move_or_extract_file(current_file,destin):
    '''
    If file choice is a valid folder, then this function is called to either move a file or extract a zip and move it

    Also double checks that the file does not exist in the destination folder before move
    :param current_file:
    :param destin:
    :return: VOID
    '''
    if destin.exists():
        if current_file.suffix == ".zip":
            temp_string = "The file or folder name in the archive(ZIP FILE) exists in the destination folder"
            write_to_file_and_print(temp_string)
        temp_string = (f"FIle exists with name: {current_file.name} in the folder {destin}")
        write_to_file_and_print(temp_string)
        temp_string =("No change made: moving to next file")
        write_to_file_and_print(temp_string)

    if not destin.exists():
        if current_file.suffix == ".zip": #mabye change this to is_zipfile()
            zf = ZipFile(current_file, 'r')
            zf.extractall(destin)
            # check if the file in zip form is there as well
            zf.close()
            temp_string = f"File Zipped into destination folder: {destin}"
            write_to_file_and_print(temp_string)
        else: #move the file
            current_file.replace(destin)
            temp_string = (f"File Moved to {destin}" )
            write_to_file_and_print(temp_string)
def prRed(skk):
    print("\033[91m {}\033[00m" .format(skk))

#open file each program call and overwrite it
with open('output_of_file_sorter.txt', 'a') as myfile:
    myfile.write("")

temp_list = path_text_file_reader()
#make it easier to read later

#path_text_file_reader returns a list of four data structures 3 lists and a dict
list_of_source_paths = temp_list[0]
dict_of_destination_paths = temp_list[1]
list_of_ignore_files = temp_list[2]
list_of_ignore_file_types = temp_list[3]

#for loop through all the source paths, then while loop the files of each source path
for i in range(len(list_of_source_paths)):
    base_dir = Path(list_of_source_paths[i]) #needs to change when the first one is done
    files = [e for e in base_dir.iterdir() if e.is_file()]

    temp_string = ("type -55 instead of a number to skip a file")
    write_to_file_and_print(temp_string)
    #temp_string = (dict_of_destination_paths)
    #write_to_file_and_print(temp_string)
    for destination in dict_of_destination_paths:
        write_to_file_and_print(dict_of_destination_paths[destination])
    index = 0
    # for loop of all source dest and go through them one at a time  - variable for current source/base?
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
                temp_string = ("invalid folder choice: re try")
                write_to_file_and_print(temp_string)
                # give them a chance to re choose
            else:
                temp_string =("Something went wrong, no changes made: retry, skip or exit")
                write_to_file_and_print(temp_string)
        except PermissionError:
            temp_string = ("Permission Denied: Win Error 5: Skipping file")
            write_to_file_and_print(temp_string)
            index = index + 1
        except ValueError:
            temp_string = ("bad input: only integers plz: retrying same file")
            write_to_file_and_print(temp_string)
        except NameError:
            temp_string = ("The number chosen is not mapped to a folder")
            write_to_file_and_print(temp_string)
            temp_string = ("Retrying same file: no changes made")
            write_to_file_and_print(temp_string)
        # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        # print(f'Got stdout: "{f.getvalue()}"')





temp_string = ("All files moved")
write_to_file_and_print(temp_string)

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