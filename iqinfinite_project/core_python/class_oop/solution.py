# CREATING A CLASS
class Phone1:
    def __init__(self,brand,model,price,quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
    def calulate_total_price(self):
        return self.price * self.quantity
    def calculate_gst(self):
        total_price = self.calulate_total_price()
        gst = total_price * (18/100)
        added_total_price_to_gst = total_price + gst
        return added_total_price_to_gst
#creating class instance
print("class Phone related stuff : ")
myphone1 = Phone1("Motorolla","Razor",1500,3)
print(f"myphone brand = {myphone1.brand}, myphone model = {myphone1.model}")
print(f"myphone price = {myphone1.price}, myphone quantity = {myphone1.quantity}")
#calcualte total price
print(f" myphone calculate total price = {myphone1.calulate_total_price()}")
print(f" myphone calculate gst price = {myphone1.calculate_gst()}")
print("\n")

# INHERITANCE
class SmartPhone1(Phone1):
    def __init__(self,brand,model,price,quantity,processor,ram,screen,battery):
        #using this super() we are accessing __init__ in the parent class so that we can insert values using constructor in the parent class
        super().__init__(brand,model,price,quantity)
        self.processor = processor
        self.ram = ram
        self.screen = screen
        self.battery = battery
# creating a class instance
print("class SmartPhone related stuff : (Inheritance)")
sp1 = SmartPhone1("Samsung","GALAXY S24 Ultra",124000,1,"snap dragon 8 gen3", "16GB LPDDR4","6.7inch","2600mAH")
print(f"sp brand = {sp1.brand}, sp model = {sp1.model}, sp processor = {sp1.processor},")
print(f"sp ram = {sp1.ram}, sp screen = {sp1.screen}, sp battery = {sp1.battery}")
print(f"sp price = {sp1.price}, sp quantity = {sp1.quantity}")
print(f"sp calculate total price = {sp1.calulate_total_price()}, sp calculate gst price = {sp1.calculate_gst()}")
print("\n")

# ENCAPSULATION
'''
Now we want that users should not be able to access brand by using class object example
class_obj = Phone("Motorolla","Razor",1500,3)
print(class_obj.brand) --> output : Motorolla

first create a getter method to access the brand attribute and set the brand attribute to private
Making brand Private: self.__brand = brand
Get brand attribute using a getter method:
def get_brand(self):
    return self.__brand
example to get a private attribute and print it in the terminal
myphone = Phone("Motorolla","Razor",1500,3)
print(f"myphone brand = {myphone.get_brand()}, myphone model = {myphone.model}")
'''
class Phone2:
    def __init__(self,brand,model,price,quantity):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__quantity = quantity
    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand

    def get_model(self):
        return self.__model
    def set_model(self,brand):
        self.__model = brand

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

    def get_quantity(self):
        return self.__quantity
    def set_quantity(self,quantity):
        self.__quantity = quantity

    def calulate_total_price(self):
        return self.__price * self.__quantity
    def calculate_gst(self):
        total_price = self.calulate_total_price()
        gst = total_price * (18/100)
        added_total_price_to_gst = total_price + gst
        return added_total_price_to_gst
print("class Phone related stuff : (Encapsulation)")
myphone2 = Phone2("Motorolla","Razor",1500,3)
'''
If you change myphone.get_model() to myphone.model then you will get AttributeError: 'Phone' object has no attribute 'model'
'''
print(f"myphone brand = {myphone2.get_brand()}, myphone model = {myphone2.get_model()}")
print(f"-->trying to change brand using myphone.brand = 'Readme' <--")
myphone2.brand = "lenovo"
print(f"myphone brand = {myphone2.get_brand()}, myphone model = {myphone2.get_model()}")
print(f"-->trying to change brand using myphone.__brand = 'Readme' <--")
myphone2.__brand = "lenovo"
print(f"myphone brand = {myphone2.get_brand()}, myphone model = {myphone2.get_model()}")
print(f"-->trying to change brand using myphone.set_brand('Readme') <--")
myphone2.set_brand("Readme")
myphone2.set_model("Note10")
myphone2.set_price(15000)
myphone2.set_quantity(4)
print(f"myphone brand = {myphone2.get_brand()}, myphone model = {myphone2.get_model()}")
print(f"myphone price = {myphone2.get_price()}, myphone quantity = {myphone2.get_quantity()}")
#calcualte total price
print(f"myphone calculate total price = {myphone2.calulate_total_price()}")
print(f"myphone calculate gst price = {myphone2.calculate_gst()}")
print("\n")

# POLYMORPHISM
'''
polymorphism means ek class kitne roop le sakta hai
'''
class Iphone(Phone2):
    def __init__(self,brand,model,price,quantity):
        super().__init__(brand,model,price,quantity)
    def os_type(self):
        return "ios"
class AndroidPhone(Phone2):
    def __init__(self,brand,model,price,quantity):
        super().__init__(brand,model,price,quantity)
    def os_type(self):
        return "android"
print("class iPhone related stuff : (Polymorphism)")
'''
you insert data for the first time in a class 
iphone = Iphone("Apple","14 pro max",174000,4)
'''
iphone = Iphone("Apple","14 pro max",174000,4)
'''
if you want to make changes in your data after the first insert then you use the method below
iphone.set_brand("Apple")
'''
print(f"IPhone brand = {iphone.get_brand()}, IPhone model = {iphone.get_model()}, IPhone os_type = {iphone.os_type()}")
print(f"IPhone price = {iphone.get_price()}, IPhone quantity = {iphone.get_quantity()}")
print(f"IPhone total price = {iphone.calulate_total_price()}, IPhone gst = {iphone.calculate_gst()}")
print("class AndroidPhone related stuff : (Polymorphism)")
android = AndroidPhone("Nothing","Phone2",51000,4)
print(f"android brand = {android.get_brand()}, android model = {android.get_model()}, android os_type = {android.os_type()}")
print(f"android price = {android.get_price()}, android quantity = {android.get_quantity()}")
print(f"android total price = {android.calulate_total_price()}, android gst = {android.calculate_gst()}")
print("\n")
'''
A better way to implement polymorphism
'''
class SmartPhone2(Phone2):
    def __init__(self,brand,model,price,quantity,processor,ram,screen):
        super().__init__(brand,model,price,quantity)
        self.__processor = processor
        self.__ram = ram
        self.__screen = screen
    def get_processor(self):
        return self.__processor
    def set_processor(self,processor):
        self.__processor = processor
    
    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram = ram
    
    def get_screen(self):
        return self.__screen
    def set_screen(self,screen):
        self.__screen = screen
    
    def os_type(self):
        if self.get_brand() == 'Apple' or self.get_brand() == "APPLE" or self.get_brand() == "apple":
            return "ios"
        else:
            return "android"
print('a better way to handle polymorphism :')
sp2 = SmartPhone2("Nothing","Phone2",51000,4,"quancomm 8th gen2","12GB","6.1 inch")
print(f"sp2 brand = {sp2.get_brand()}, sp2 model = {sp2.get_model()}, sp2 os_type = {sp2.os_type()}")
print(f"sp2 price = {sp2.get_price()}, sp2 quantity = {sp2.get_quantity()}")
print(f"sp2 total price = {sp2.calulate_total_price()}, sp2 gst = {sp2.calculate_gst()}")
sp3 = SmartPhone2("Apple","14 pro max",151000,4,"Apple A14","8GB","5.8 inch")
print(f"sp3 brand = {sp3.get_brand()}, sp3 model = {sp3.get_model()}, sp3 os_type = {sp3.os_type()}")
print(f"sp3 price = {sp3.get_price()}, sp3 quantity = {sp3.get_quantity()}")
print(f"sp3 total price = {sp3.calulate_total_price()}, sp3 gst = {sp3.calculate_gst()}")
print("\n") 

# CLASS VARIABLE
'''
create a parent class variable to keep track of number of phones created
'''
class Phone3:
    '''
    decalring a class variables in the parent class here in this case Phone3
    '''
    total_phone = 0
    def __init__(self,brand,model,price,quantity):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__quantity = quantity
        '''How to access and perform operation on class variables inside the class'''
        Phone3.total_phone += 1
    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand

    def get_model(self):
        return self.__model
    def set_model(self,brand):
        self.__model = brand

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

    def get_quantity(self):
        return self.__quantity
    def set_quantity(self,quantity):
        self.__quantity = quantity

    def calulate_total_price(self):
        return self.__price * self.__quantity
    def calculate_gst(self):
        total_price = self.calulate_total_price()
        gst = total_price * (18/100)
        added_total_price_to_gst = total_price + gst
        return added_total_price_to_gst

class SmartPhone3(Phone3):
    def __init__(self,brand,model,price,quantity,processor,ram,screen):
        super().__init__(brand,model,price,quantity)
        self.__processor = processor
        self.__ram = ram
        self.__screen = screen
    def get_processor(self):
        return self.__processor
    def set_processor(self,processor):
        self.__processor = processor
    
    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram = ram
    
    def get_screen(self):
        return self.__screen
    def set_screen(self,screen):
        self.__screen = screen
    
    def os_type(self):
        if self.get_brand() == 'Apple' or self.get_brand() == "APPLE" or self.get_brand() == "apple":
            return "ios"
        else:
            return "android"
print('Class Variable : keep track of number of phones created')
sp2_class_variable = SmartPhone3("Nothing","Phone2",51000,4,"quancomm 8th gen2","12GB","6.1 inch")
print(f"sp2_class_variable brand = {sp2_class_variable.get_brand()}, sp2_class_variable model = {sp2_class_variable.get_model()}, sp2_class_variable os_type = {sp2_class_variable.os_type()}")
print(f"sp2_class_variable price = {sp2_class_variable.get_price()}, sp2_class_variable quantity = {sp2_class_variable.get_quantity()}")
print(f"sp2_class_variable total price = {sp2_class_variable.calulate_total_price()}, sp2_class_variable gst = {sp2_class_variable.calculate_gst()}")
sp3_class_variable = SmartPhone3("Apple","14 pro max",151000,4,"Apple A14","8GB","5.8 inch")
print(f"sp3_class_variable brand = {sp3_class_variable.get_brand()}, sp3_class_variable model = {sp3_class_variable.get_model()}, sp3_class_variable os_type = {sp3_class_variable.os_type()}")
print(f"sp3_class_variable price = {sp3_class_variable.get_price()}, sp3_class_variable quantity = {sp3_class_variable.get_quantity()}")
print(f"sp3_class_variable total price = {sp3_class_variable.calulate_total_price()}, sp3_class_variable gst = {sp3_class_variable.calculate_gst()}")
sp4_class_variable = SmartPhone3("Apple","14 pro max",151000,4,"Apple A14","8GB","5.8 inch")
print(f"sp4_class_variable brand = {sp4_class_variable.get_brand()}, sp4_class_variable model = {sp4_class_variable.get_model()}, sp4_class_variable os_type = {sp4_class_variable.os_type()}")
print(f"sp4_class_variable price = {sp4_class_variable.get_price()}, sp4_class_variable quantity = {sp4_class_variable.get_quantity()}")
print(f"sp4_class_variable total price = {sp4_class_variable.calulate_total_price()}, sp4_class_variable gst = {sp4_class_variable.calculate_gst()}")
'''
This is how you access class variables outside the class
We should not access the class variables via class object instead we should access the class variables 
by directly using class.
Now why is that ?
The reason is simple If we access the class variables like that then we may or may not get the accurate answers
because of the way how the classes and objects work in python.
'''
print(f"Number of phones created : {Phone3.total_phone}")
print("\n") 