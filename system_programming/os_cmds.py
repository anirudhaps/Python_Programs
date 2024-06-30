import os

# print the OS name
print("OS:", os.name)

# print the current working directory
print("CWD:", os.getcwd())

# change the dir and print CWD
os.chdir("/home/anirudha/develop/")
print("Listing the contents of the CWD:", os.getcwd())
#print(os.listdir())
for f in os.listdir():
    print(f)

if os.path.exists("/home/anirudha/develop/gocode/README.md"):
    print("/home/anirudha/develop/gocode/README.md file exists!")
else:
    print("file does not exists.")