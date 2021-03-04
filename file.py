import os
import shutil
from tempfile import TemporaryFile


#file systems

#pwd
print("The pwd command ", os.getcwd())

#ls
print("The ls command", os.listdir())

#ls -R
print("The ls -R command", os.walk("starting_directory_path"))

#cd
print("changing the directory to parent")
os.chdir("/Users/apple/PycharmProjects")

#pwd again
print("The pwd command ", os.getcwd())

#mkdir
print("making a directory mkdir -p command")
os.makedirs("/Users/apple/PycharmProjects/newdir")

#check creation by cd
os.chdir("/Users/apple/PycharmProjects/newdir")

#pwd again
print("The pwd command ", os.getcwd())

#cp command
shutil.copy2("/Users/apple/Downloads/alphabet.png", "/Users/apple/Desktop/alphabet.png")

#cd to desktop and ls to check
#cd
print("changing the directory to parent")
os.chdir("/Users/apple/")
print("changing the directory to desktop")
os.chdir("/Users/apple/Desktop")

#ls
if "alphabet.png" in os.listdir():
    print("copy made")
else:
    print("copy not made")

#remove from desktop
os.remove("alphabet.png")
#ls
if "alphabet.png" in os.listdir():
    print("not deleted")
else:
    print("deleted")

#finally deleteing the directory made
os.chdir("/Users/apple/")
os.chdir("/Users/apple/PycharmProjects")
shutil.rmtree("/Users/apple/PycharmProjects/newdir")

#os.chdir("/Users/apple/PycharmProjects/newdir")
os.chdir("/Users/apple/")
os.chdir("/Users/apple/Desktop")
print("The pwd command ", os.getcwd())


# Create a temporary file and write some data to it
fp = TemporaryFile('w+t')
fp.write('Hello')

# reading
fp.seek(0)
data = fp.read()

# Closing
fp.close()


#reading and writing from a file
file = open('hello.txt','w')
file.write("hello")
file.close()

file = open('hello.txt','r')
print(file.read())
file.close()





