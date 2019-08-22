import shutil
import time
import os

rootdir = "/home/strahinja/Desktop/git/sudoku_solver/new_digits/"
final = "/home/strahinja/Desktop/git/sudoku_solver/new_digits/"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        for i in range(1000):
            if file[-3:] == "png":
                name = str(time.time()) + "_" + file[:-4] + ".png"
                shutil.copy(os.path.join(final, file), name)
