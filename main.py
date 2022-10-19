from tokenize import String
from xml.etree.ElementTree import tostring
import numpy as np
from myNN import NNetwork
from myNN import NNLayer 
from random import randrange
from math import floor
import os
os.system('clear')


"""
nn = NNetwork([2,4,1])

for i in range(100000):
    x = randrange(2)
    y = randrange(2)
    input = np.array([[x],[y]])
    t = 0 if x == y else 1
    target = np.array([[t]])
    nn.train(input,target, 0.001)

input = np.array([[0],[1]])
guess = nn.guess(input)

print(guess)
"""

nn = NNetwork([1,2,1])

inputAge = input("Enter your age: ")
guess = nn.guess(inputAge)
print("Your age is probly not "+ str(guess[0][0]))


for i in range(100000):
    age = randrange(50)
    inputData = np.array([[age]])
    targetData = np.array([[age]])
    nn.train(inputData, targetData, 0.0001)

print("My AI can Guess you age, giving age as input")
inputAge = input("Enter your age: ")
guess = nn.guess(inputAge)
print("Your age is "+ str(int(round(guess[0][0]))))
err = inputAge-guess[0][0]
margin = abs(err / inputAge)
print("Accuracy: " + str(1-margin) + "%")
