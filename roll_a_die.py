import random
import statistics
# from looper import whiler
# from random import choice

# We can either import an entire library or just a part of it eg a fn 
die = random.choice([1,2,3,4,5,6])
# die = choice([1,2,3,4,5,6])
print(f"Die Value: {die}")

# whiler(die)

rnum = random.randint(-1,1)
print(f"Random Int: {rnum}")

cards = ["J", "K", "Q", "10"]
print(cards)
random.shuffle(cards)
print(cards)

# diff module to cal  mean
print(statistics.mean([1,10]))