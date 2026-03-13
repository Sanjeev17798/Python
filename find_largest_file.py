# This will find the largest file into current directory 
import os

largest_file = ""
largest_size = 0

for file in os.listdir():
    if os.path.isfile(file):
        size = os.path.getsize(file)
        if size > largest_size:
            largest_size = size
            largest_file = file

print("Largest file:", largest_file)
print("Size:", largest_size, "bytes")

# agar user sy input dena hai like need to puth path we can just put as on top path=input("")