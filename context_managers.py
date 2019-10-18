# TASK
# Practice Activity: Context Managers
#
# For this activity, the task is simple. Create the context manager for creating temporary files. The logic for this was described in the previous video.
#
#
# Note that while we have the code for this in the notebook, you should try to do this yourself before looking at that code.

import shutil
import tempfile
import os

from contextlib import contextmanager

@contextmanager
def temp_dir():
    try:
        name =tempfile.mkdtemp()
        print("temp dir:{}".format(name))
        cwd = os.getcwd()
        temp_dir_name = os.path.join(cwd,name)
        print("Dir before yield:")
        for dir in os.scandir(cwd):
            print( dir)
        
        os.chdir(temp_dir_name)

        with open(os.path.join(temp_dir_name,"text.txt"), "w") as f:
            yield f

        print("Temp file contents:")

        with open(os.path.join(temp_dir_name, "text.txt"), "r") as f:
            z = f.readlines()
            for line in z:
                print(line)






        print("Dir after yield:")
        for dir in os.scandir(cwd):
            print(dir)

    finally:
        shutil.rmtree(temp_dir_name)
        print("Dir after:")
        for dir in os.scandir(cwd):
            print( dir)
    return

if __name__ == "__main__":
    with temp_dir() as fl:
        fl.write("Hello from temp file")
        fl.write("hello,hello,hello")

