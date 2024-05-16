from item import Item
#inherit from Item class
class phone(Item):
    #polymorphism overriding pay_rate
    pay_rate = 0.5
    all_phone_instances = []
    def __init__(self, name : str, price: float, quantity=0, broken_phones = 0):
        #call the super function to have all the attributes/methods of the parent class
        super().__init__(name, price, quantity)
        #run validations to the recieved arguments in the constructor
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than zero!"
        #Assign to self object
        self.broken_phones_ = broken_phones
        phone.all_phone_instances.append(self)
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity_}')"
    
