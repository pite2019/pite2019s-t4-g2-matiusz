#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

def MatrixSize2():
  def __init__(self, upleft, upright, downleft, downright):
    self.val = [MatrixColumnSize2(upleft, downleft), MatrixColumnSize2(upright, downright)]
  @static
  def ZerosMatrix():
    return MatrixSize2(0,0,0,0)
  def add(self, matrix):
    for i in range(2):
      for j in range(2):
         self.val[i][j] += matrix.val[i][j]
  def product(self, matrix):
    result = ZerosMatrix()
    for i in range(2):
      for j in range(2):
        for k in range(2):
          result.val += self.val[k][j]*matrix.val[i][k]
    self = result
def MatrixColumnSize2():
  def __init__(self, first, second):
    self.Column = [first, second]
      
