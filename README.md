Program for organizing many files in a group of folders where doing it with the mouse 
might be annoying and time consuming. It also would be good in environments where
users have access only to a terminal. a GUI version will come when this version is 
completed.

The program reads from a text file to take in information to know which paths 
to moves files to and which folders to move files from. It can also know which 
files to ignore and which file types.


sort.py and testing_csv.py  -- are the main files to look at.

i was going to and still may use a csv instead of a text file


file_path_organizer.py

    Reads the text file and  organizes the 
    paths in the text file  into data structures to be used 
    in sort.py
    
sort.py
    loops over the number of source folder entries and moves 
    the files as requested.