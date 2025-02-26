import os
path = os.getcwd()
print(path)
os.chdir('..')
path_2 = os.getcwd()
print(path_2)