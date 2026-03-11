import os
filename=input("filename:")
cwd=os.getcwd()
def find(filename):
    for f in os.listdir(cwd):
        if f==filename:
            return os.path.join(cwd , f)
        return None

file_path= find(filename)
if file_path:
    print("Filepath", file_path)
    with open(file_path , "r") as file:
        line_count = sum(1 for _ in file)
    print("Total number of lines:", line_count)

else:
    print("Not found")


