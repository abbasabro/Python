# import Utils as ut
import random as r
# numbers=[2,5,3,7,1,6]
# print(ut.find_max(numbers))

class Dice:
    def roll(self):
        numbers=(1,2,3,4,5,6)
        value1=r.choice(numbers)
        value2=r.choice(numbers)
        return f"({value1},{value2})"
    
    
ludo=Dice()
print(ludo.roll())    