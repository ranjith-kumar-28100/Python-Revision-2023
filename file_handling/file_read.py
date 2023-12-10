import os,sys
if os.path.isfile('file.txt'):
    f = open('file.txt', 'r')
else:
    print("File doesn't exit")
    sys.exit()

content = f.read()
print(content)
f.close()