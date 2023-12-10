class Product:
    def __init__(self):
        self.name = 'Royal Enfield'
        self.desc = 'Motor Bike'
        self.price = 2_50_000

    def __del__(self):
        print("Destructing the Product Object")
    def display(self):
        print(self.name)
        print(self.desc)
        print(self.price)


p1 = Product()
# print(p1.name, p1.desc, p1.price)
p1.display()
p1 = None
p2 = Product()
p2.name = "Mercedes Benz"
p2.desc = "Luxury Motor Car"
p2.price = 2_50_00_000
# print(p2.name, p2.desc, p2.price)
p2.display()
