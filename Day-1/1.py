class Computer:

    def config(self):
        print("i5, 8gb, 1TB")

com1 = Computer()
# com2 = Computer()
print(type(com1))

a = 1
print(type(a))

Computer.config(com1)
# Computer.config(com2)

# com1.config()
# com2.config()

# print(a.bit_length())