import os
cwd=os.getcwd()

files=[f for f in os.listdir() if os.path.isfile(f)]
print("Number of files", len(files))


#f is just a variable name used in a list comprehension.It represents each file name returned by os.listdir().
# [] collects results and stores them in a list., [] here creates a list by looping through items.
# its counting the no of files with extantion .py you can put txt etc.