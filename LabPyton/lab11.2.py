from turtle import *
from random import randint
shape("turtle")
colors = ["blue", "red", "orange", "purple"]
shredder = randint(1,10)
user_choose = 0
while user_choose != shredder:
 user_choose = str.lower(input("select direction Left/Right/Direct/Back - "))
