from os import listdir, walk
from os.path import isfile, join
import os

mypath="/Users/kpodlaska/PycharmProjects/pythonProject/Capstone"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)


filenames = next(walk(mypath), (None, None, []))[2]
print(filenames)

directory = os.path.abspath('./')
print(directory)
