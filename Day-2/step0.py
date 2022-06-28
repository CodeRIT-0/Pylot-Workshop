import random


x = random.randint(1,100)

# print(x)
print([random.randint(1,100) for _ in range(100)])



def randomizer(n,lim):
    return [random.randint(1,lim) for x in range(n)]