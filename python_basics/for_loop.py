countries = ['India', 'America', 'England', 'Singapore', 'Japan', 'Australia']
for country in countries:
    print(country)

for i in range(1, 26):
    print(i)

for i in range(len(countries)):
    print(countries[i])

dict_ = {'name': 'Ranjith Kumar', 'initial': 'G', 'shortform': 'rkg'}
for k, v in dict_.items():
    print(f"{k} : {v}")

list_ = [8, 9, -6, 5, 3]
prod = 1
for i in list_:
    prod *= i
print(prod)

n = int(input("enter a  number: "))
for i in range(1, 11):
    print(f"{i} * {n} = {i * n}")
