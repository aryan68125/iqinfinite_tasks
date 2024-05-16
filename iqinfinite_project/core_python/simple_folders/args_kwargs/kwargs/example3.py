'''
Using **kwargs in Python to set values of object
'''
# defining car class
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']


# creating objects of car class
audi = Car(s=200, c='red')
bmw = Car(s=250, c='black')
mb = Car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)