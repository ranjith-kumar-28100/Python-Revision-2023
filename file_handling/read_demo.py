f = open('sample.txt','r')
print(f.read())
f.seek(0)
print('#######################################################')
content = f.readline()
while content != '':
    print(content)
    content = f.readline()
f.seek(0)
print('#######################################################')
lines = f.readlines()
print(lines)
f.close()