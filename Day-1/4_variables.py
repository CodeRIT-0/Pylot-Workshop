class Car:
    wheels= 4 #class or static variables
    def __init__(self,mil,comp):
        self.mil = mil 
        self.com = comp



c1 = Car(10,"BMW")
c2 = Car(20,"Mercedes")

print(c1.mil)
print(c2.mil)
print(Car.wheels)


# c1.mil = 8
# Car.wheels = 5

# print(c1.com,c1.mil,Car.wheels)
# print(c2.com,c2.mil,c2.wheels)