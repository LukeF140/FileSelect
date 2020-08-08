# Imports
import shutil, os, random, re

# Variables & Arrays
picFileExten = [".JPG", ".PNG"]
getDir = []

# Main
try:
    readFile = open("Directorys.txt", "r")
    fileCont = readFile.readlines()
    # Remove \n
    for E in fileCont:
        E = re.sub('\\n', '', E)
        if E != ' ' or E != '':
            getDir.append(E)

    if len(getDir) < 1:
        getDir.append(input("Please Enter a Directory to Get Images From: "))
except FileNotFoundError:
    getDir.append(input("Please Enter a Directory to Get Images From: "))


placeDir = input("Please Enter a Directory to Place Images: ")


total, used, free = shutil.disk_usage(placeDir)
full = total * 0.7

print("")

files = []
totalFileSpace = 0
for direct in getDir:
    print("GETTING PICTURES FROM: " + direct)
    for root, subfolders, filenames in os.walk(direct):
        for file in filenames:
            filename, fileExtension = os.path.splitext(file)
            if fileExtension.upper() in picFileExten:
                totalFileSpace += os.path.getsize(root + "\\" + file)
                files.append(root + "\\" + file)


print("GOT PICTURES\n\nCHOSING & COPYING PICTURES")
if totalFileSpace < free and totalFileSpace < full:
    num = 1
    for file in files:
        print("(" + str(num) + " of " + str(len(files)) +") COPYING: " + file)
        shutil.copy(file, (placeDir + os.path.basename(file)))
        num += 1
else:
    pics = []
    picNames = []
    total, used, free = shutil.disk_usage(placeDir)
    while used < full:
        file = random.choice(files)
        if not(file in pics) and not(os.path.basename(file) in picNames):
            print("(" + str(int((used/full) * 100)) + "%) COPYING: " + file)
            pics.append(file)
            picNames.append(os.path.basename(file))
            shutil.copy(file, placeDir + os.path.basename(file))
            
        total, used, free = shutil.disk_usage(placeDir)
