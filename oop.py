class SimpleClass:
    pass

class Person:
    pass

class Animal:
    def first_method(self):
        pass

class Classey:
    varia = 2

    def method(self):
        print(self)

object_one = Classey()
object_two = Classey()

object_one.varia = 3
object_two.varia = 5

print(object_one.varia)
print(object_two.varia)

class Transport:
    def _init_(self, air, water):
        self.air = air
        self.water = water

obj_transport = Transport(air="Beluga", water="Hovercraft")
obj2 = Transport(air="Jet", water="Boat")

print(obj_transport.air, obj_transport.water)
print(obj2.air, obj2.water)

class Person:
    def init(self, fname, lname):
        self.fname = fname
        self.lname = lname



class ShoppingCart:
    def _init_ (self):
        self.items=[]

    def add_item(self,item_name,qty):
       item=(item_name,qty)

    def remove_item(self,item_name):
        for item in self.items:
            if item[0]==item_name:
                self.items.remove(item)
                break
   #cThis method computes the number of items in our cart
    def calculate_total(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total

cart=ShoppingCart()

cart.add_item(item_name="Kiwi",qty=100)
cart.add_item(item_name="Papaya",qty=100)
cart.add_item(item_name="Orange",qty=100)

print("Current Items in Cart")
for item in cart.items:
    print(item[0],"-", item[1])

total_qty=cart.calculate_total()
print("Total Quantity:",total_qty)