import unittest
from file_path_organizer import *

#have a debug mode for automating input on the folder choice

class test_ignored_file_types_dont_move(unittest.TestCase):


    #add a setup and tear down for this one


    def test_source_only_has_ignored_files(self):
        #create a set amount of files (random mabye?) of certain file type

        items = ["one", "two", "three","four","five"]

        for item in items:
            with open(f"C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/testing_only_ignored_file_types/Source/{item}.txt", "w") as f:
                f.write("This is my first line of code")

        path_text_file_reader("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/testing_only_ignored_file_types/ignored_file_types.txt")

        source = Path("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/testing_only_ignored_file_types/Source")

        #compare destination folder is = to what it should be
        files = [e for e in source.iterdir() if e.is_file()]
        assert (len(files) == len(items))

        #delete all file sin source or destination
        for file in files:
            file.unlink()

if __name__ == '__main__':
    unittest.main()