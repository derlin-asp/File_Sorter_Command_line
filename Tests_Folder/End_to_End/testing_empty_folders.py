import unittest
from file_path_organizer import *

#have a debug mode for automating input on the folder choice

class test_empty_Source_folders_dont_affect_destination_folders(unittest.TestCase):


    def test_empty_source(self):
        #give it empty folder and asser there empty first
        destin_path = Path("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/Empy_Source_Folders/Destination")
        source1 = Path("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/Empy_Source_Folders/Source1")
        files = [e for e in source1.iterdir() if e.is_file()]
        assert(files == [])

        #this one should also be empty
        source2 = Path("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/Empy_Source_Folders/Source1")
        files = [e for e in source2.iterdir() if e.is_file()]
        assert (files == [])

        #tell it to use two empty folders to move files from
        path_text_file_reader("C:/Users/david/PycharmProjects/File_Fixer/Folder_For_Tests_Only/Empy_Source_Folders/empty_test_file.txt")


        #assert that the destination folder is still empty
        files = [e for e in destin_path.iterdir() if e.is_file()]
        print(files)
        assert(files == [])


if __name__ == '__main__':
    unittest.main()