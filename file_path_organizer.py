import pprint
from pathlib import *
from user_error_checking import check_for_path_errors_in_sources


def path_text_file_reader(input_file = "text-finder-300079.txt"):
    '''
    Reads text file and creates a list of paths and files to be used in the program.
    '''
    with open(input_file, "r") as f:
        list_of_paths = [line.strip() for line in f if line.strip()]


    source_path_list = []
    destination_path_dict = {}
    ignore_path_list = []
    ignore_file_type_list = []

    no_no_list = ["destinations", "ignore", "source"]

    destination_count = 1
    folder_flag = ""
    for line in range(len(list_of_paths)):

        if list_of_paths[line].lower() == "destinations":
            folder_flag = "DESTINATIONS"
        if list_of_paths[line].lower() == "ignore":
            folder_flag = "ignore"
        if list_of_paths[line].lower() == "source":
            folder_flag = "source"


        if folder_flag == "source" and list_of_paths[line].lower() not in no_no_list\
            and check_for_path_errors_in_sources(list_of_paths[line]):
                source_path_list.append(list_of_paths[line])

        elif folder_flag == "DESTINATIONS" and list_of_paths[line].lower() not in no_no_list:
            try:
               temp_dest_path = Path(list_of_paths[line])
               if temp_dest_path.is_dir():
                   destination_path_dict.update({ destination_count : list_of_paths[line]  })
                   destination_count = destination_count + 1
               else:#then make the directory
                    print("Trying to make a new directory.")
                    temp_dest_path.mkdir(parents=True)
                    destination_path_dict.update({destination_count: list_of_paths[line]})
                    destination_count = destination_count + 1
            except FileExistsError:
                print("Creating directory failed, double check folder structure")
        elif folder_flag == "ignore" and list_of_paths[line].lower() not in no_no_list:
            ignore_path_list.append(list_of_paths[line])

        else:
            print("Issue with flag or blanks") #printing at end of file always, no affect noticed on accuracy


    for file in ignore_path_list:
        temp_path = Path(file)
        if temp_path.stem == "*":
            ignore_file_type_list.append(temp_path.suffix)

    #print(ignore_file_type_list)






    return [source_path_list, destination_path_dict, ignore_path_list,ignore_file_type_list]

#path_text_file_reader()



# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(path_text_file_reader())


