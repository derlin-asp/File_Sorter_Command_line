from pathlib import *

# base_dir = Path("C:/Users/david/Desktop/xxx")
#
#
#
# files = [e for e in base_dir.iterdir() if e.is_dir()]
#
#
# print(files)


'''
if file ends in zip

unzip before moving
'''
test_path = Path('C:/Users/david/Desktop/source2/gui-inspect-tool-master.zip')

print(test_path.suffix)

from zipfile import ZipFile
zf = ZipFile(test_path, 'r')
zf.extractall('C:/Users/david/Desktop/xxx')
zf.close()


