class MatrixSize2():
  def __init__(self, upleft, upright, downleft, downright):
    self.row = [MatrixColumnSize2(upleft, downleft), MatrixColumnSize2(upright, downright)]
  
  @staticmethod
  def ZerosMatrix():
    return MatrixSize2(0,0,0,0)
  def add(self, matrix):
    for i in range(2):
      for j in range(2):
         self.row[i].col[j] += matrix.row[i].col[j]
    return self
  def product(self, matrix):
    result = MatrixSize2.ZerosMatrix()
    for i in range(2):
      for j in range(2):
        for k in range(2):
          result.row += self.row[k].col[j]*matrix.row[i].col[k]
    self = result
    return self
  def __str__(self):
    return str(self.row[0].col[0])
class MatrixColumnSize2():
  def __init__(self, first, second):
    self.col = [first, second]

    
def Main():
  matrix1 = MatrixSize2(1,2,3,4)
  matrix2 = MatrixSize2(11,12,13,14)
  print(matrix1)
  print(matrix2)
  print(matrix1.add(matrix2))
  print(matrix1.product(matrix2))

  
if __name__=="__main__":
  Main()
