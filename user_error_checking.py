from pathlib import Path


####Source path checking

#new_list = [expression(i) for i in old_list if filter(i)]
def check_for_bad_characters(current_path):
    list_of_illegals = [ '<','>',':','"','/','\\', '|','?','*' ]
    print(list_of_illegals)
    bad_list = [ char for char in current_path if(char in list_of_illegals)  ]

    return bad_list

def get_number_of_files_in_path(current_path):
    files = [e for e in current_path.iterdir() if e.is_file()]
    return len(files)

def check_for_path_errors_in_sources(path_as_string):
    path_as_path_obj = Path(path_as_string)

    bad_chars = check_for_bad_characters(path_as_string)
    if  len(bad_chars) > 0:
        return 0,f"There are imroper characters in the path: {bad_chars}"

    elif not path_as_path_obj.is_dir(): #if exists and if it is a dir
        return 0 , "Not valid Directory"  #returns tuple with code and message

    elif get_number_of_files_in_path(path_as_path_obj) == 0:
        return 1,"No Files in Source Directory"


