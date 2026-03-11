import os 
filename=input("filename:")
cwd=os.getcwd()

def find_file(filename):
    for f in os.listdir(cwd):
        if f==filename:
            return os.path.join(cwd , f)
        return None 
    
result=find_file(filename)
print("Result is ", result)
