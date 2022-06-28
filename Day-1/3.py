class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

    def update(self,newage):
        self.age = newage

p1 = Person("Subinoy",20)

# p1.age = 29
p2 = Person("Jayant",60)
p2.update(20)

print(p1.compare(p2))