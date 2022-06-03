import os

path = "/Volumes/UME/Tokyo Ghoul/staffel 3"
name = str(input("Enter the name of the file: "))

def walkFolder(path):
    for files in os.walk(path):
        l = files[2:]
        count = 0
        sorted_l = sorted(l[0])
        for file in sorted_l:
            if file.startswith("."):
                continue
            else:
                count += 1
                print(file)
                print(count)
                #rename_files(count, file) # uncomment this line to rename files

def rename_files(count, file):
    if count < 10:
        newName = name + "_00" + str(count) + ".mkv"
    elif count < 100:
        newName = name + "_0" + str(count) + ".mkv"
    else:
        newName = name + "_" + str(count) + ".mkv"
    os.rename(path+"/"+file, path+"/"+newName)

walkFolder(path)
