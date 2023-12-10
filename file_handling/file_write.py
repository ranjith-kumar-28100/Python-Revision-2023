f = open('file.txt', 'w')
inp = ''
print("Enter the message: (Type # when you are done) ")
while inp != '#':
    inp = input()
    if inp != '#':
        f.write(inp+"\n")
f.close()