#file for testing new csv feature

# source_paths_map = {}

# with open('text-finder-300079.txt', 'r') as reader:
#     list_of_paths = reader.read().splitlines()
#

with open("text-finder-300079.txt", "r") as f:
    list_of_paths = [line.strip() for line in f if line.strip()]




# from collections import defaultdict
# d = defaultdict(int)
#
#
# print(d)
#
#
#
# for x in range(0,11):
#     d[x] == ""
source_path_list = []
destination_path_dict = {}
ignore_path_list = []


no_no_list = ["destinations", "ignore", "source","DESTINATIONS"]

destination_count = 0
folder_flag = "source"
for line in range(len(list_of_paths)):

    if list_of_paths[line].lower() == "destinations":
        folder_flag = "DESTINATIONS"
    if list_of_paths[line].lower() == "ignore":
        folder_flag = "ignore"

    if folder_flag == "source":
        temp = list_of_paths[line].lower()
        if temp not in no_no_list:
           source_path_list.append(list_of_paths[line])

    elif folder_flag == "DESTINATIONS":
        temp = list_of_paths[line]
        print(temp)
        if temp not in no_no_list:
            destination_path_dict.update({ destination_count : list_of_paths[line]  })
            destination_count = destination_count + 1

    elif folder_flag == "ignore" and list_of_paths[line].lower() not in no_no_list:
        ignore_path_list.append(list_of_paths[line])

    else:
        print("Issue with flag or blanks")

print(list_of_paths)
print(ignore_path_list)
print(destination_path_dict)
print(source_path_list)
# dict_of_paths = {}
# for i,e in enumerate(list_of_paths):  #proba better way of putting it into a dic in one go
#     dict_of_paths.update({i:e})
#
