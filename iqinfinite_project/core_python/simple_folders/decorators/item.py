import csv
#creation of the class
class Item:
    #create a list of instances that will hold all the instances of a class
    all_instanes_Item_class = []
    #creating a class attribute:
    pay_rate = 0.8 #pay rate after 20% discount

    def __init__(self, name : str, price: float, quantity=0):
        #run validations to the recieved arguments in the constructor
        assert price >=0, f"Price {price} is not greater than zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than zero!"
        #Assign to self object
        self.__name = name
        self.__price = price
        self.quantity_ = quantity

        #append the instance as soon as it's created
        #self is acutally instance itself every time that is being created.
        Item.all_instanes_Item_class.append(self)

    @property
    def name(self):
        print("get an attribute")
        return self.__name
    @property
    def price(self):
        return self.__price
    
    @name.setter
    def name(self, value):
        print("set an attribute")
        if len(value) > 10:
            raise Exception("The name exceeds the max length of 10 characters")
        self.__name = value

    @price.setter
    def value(self, value):
        if value < 0:
            raise Exception("Price cannot be negative")
        self.__price = value

    def calculate_total_price(self):
        return self.__price*self.quantity_
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    #increment_value comes from outside not from the class constructor
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @classmethod
    def instanciate_from_csv(cls):
        # write the code to read the csv file and instanciate some objects
        #use the context manager to read the item.csv file
        #with open('file_name.csv', 'permission')as f:
        #csv.DictReader(f) --> this will read our content f as a list of dictionary
        with open('items.csv', 'r')as f:
            #read the csv and convert it to a python dictionary
            reader = csv.DictReader(f)
            #convert this dictionary into a list
            items=list(reader)
        for item in items:
            print(item)
        #instantiate the object from csv
        for item in items:
            Item(
                name=item.get('name'),
                __price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        #count out the float that have .0 example 5.0, 4.0
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.__price}', '{self.quantity_}')"
    
    #abstraction
    #making methods private using double underscore
    def __connect(self,smtp_server):
        pass
    def __prepare_body(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.__price}', '{self.quantity_}')"
    def __send(self):
        pass
    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()