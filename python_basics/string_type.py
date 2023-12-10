name = "Ranjith"
print(f"Name: {name}",type(name),len(name))
quote = '''Honesty
Truthiness
Hardwork
Are the best human qualities to have.'''
print(quote)
print(len(quote))
print(quote[0])
print(quote[10])
print(quote[-1])
print(quote[0:7])
print(quote[-5:-1])
print(quote[0::5])
print(name[::-1])
print(name[0:])
print(name[:7])
name = " Ranjith "
print(name)
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print(name.find("jith",1,len(name)-1))
print(name.find("jiith",1,len(name)-1))
print(name.count(' '))
print(name.replace(' ','_'))
print(name)
print(name.upper())
print(name.lower())
print(name.strip()[1:].capitalize())