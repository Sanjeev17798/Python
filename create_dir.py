import os
try:
    os.mkdir("test")              # Try to create the directory
    print("created")              # Success message
except FileExistsError:
    print("no its already there") # Directory already exists
except Exception as e:
    print("failed")               # Catch any other errors
