from random import random,choice
class Pound:
    def __init__(self):
        self.color = "gold"
        self.value = 100
        self.tax = 1000
        self.head=True

    def rust(self):
        self.color = "black"
    def __del__(self):
        print("spent coin")
    def choose(self):
        poss=[True,False]
        self.head=choice(poss)

coin1 = Pound()
coin1.color = "maroon"
print(coin1.color)  # Output: maroon

coin2 = Pound()
print(coin2.color)  # Output: gold

coin1.rust()  # Call the rust method on coin1
print(coin1.color)  # Output: black

del coin2



