import shutil
import os

def disk():
    total ,used , free =shutil.disk_usage("/home")
    print("Disk total ",total //(2**30),"Gib")
    print("disk used",used //(2**30),"Gib")

disk()
#1 KB = 2¹⁰ bytes = 1024 bytes
#1 MB = 2²⁰ bytes = 1,048,576 bytes
#1 GiB = 2³⁰ bytes = 1,073,741,824 bytes


