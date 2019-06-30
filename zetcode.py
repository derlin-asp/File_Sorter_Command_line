

#taken form http://zetcode.com/python/pathlib/


from pathlib import Path
from os import chdir

#info on f strings   https://realpython.com/python-f-strings/

print(f"Current directory: {Path.cwd()}") #print cwd
print(f"Home directory: {Path.home()}") #print home directory




path = Path('..')  #path = .. for cd

chdir(path)

print(f'Current working directory: {path.cwd()}')

path = Path.home()
docs = path / 'Documents'  #docs = home + documents


print(docs)



path = Path("C:/Users/david/Desktop/New folder")

home = Path.home()

relative = path.relative_to(home)
print(relative)

relative = path.relative_to(home)
print(relative)

