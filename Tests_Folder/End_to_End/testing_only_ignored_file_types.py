import unittest
from file_path_organizer import *
import time
#have a debug mode for automating input on the folder choice

class test_ignored_file_types_dont_move(unittest.TestCase):


    #add a setup and tear down for this one


    def test_source_only_has_ignored_files(self):
        #create a set amount of files (random mabye?) of certain file type

        items = ["one", "two", "three","four","five"]


        #create some txt files in source folder to be ignored
        for item in items:
            with open(f"C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/testing_only_ignored_file_types/Source/{item}.txt", "w") as f:
                f.write("This is my first line of code")


        source = Path("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/testing_only_ignored_file_types/Source")

        #grab the files in source before the program is called
        source_files =  [e for e in source.iterdir() if e.is_file()]

        #time.sleep(1111)
        #call the program
        path_text_file_reader("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/testing_only_ignored_file_types/ignored_file_types.txt")



        #compare destination folder is = to what it should be
        files = [e for e in source.iterdir() if e.is_file()]
        assert (len(files) == len(items))
        assert(source_files == files)

        #delete all file sin source or destination
        for file in files:
            file.unlink()

        #check if destination is empty
        destin = Path("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/testing_only_ignored_file_types/Destination")
        files_in_destination = [e for e in destin.iterdir() if e.is_file()]

        assert (files_in_destination == [])

if __name__ == '__main__':
    unittest.main()