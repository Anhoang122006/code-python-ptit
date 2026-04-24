import sys

class Matrix:
  def __init__(self,n,m,data):
    self.n=n
    self.m=m
    self.data=data
  def get_transpose(self):
    transpose_data=[]
    for i in range(n):
      new_row=[]
      for j in range(m):
        new_row.append(self.data[j][i])
      transpose_data.append(new_row)
    return Matrix(self.m,self.n,transpose_data)
  def multiphy(self,other):
    res_data=[]
    for i in range(self.n):
      res_row=[]
      for j in range(other.m):
        cell_value=0
        for k in range(self.m):
          cell_value=self.data[i][k]*other.data[k][j]
          res_row.append(cell_value)
        res_data.append(res_row)
    return(self.n,other.m,res_data)
  def display(self):
    for row in self.data:
      print(" ".join(map(str,row)))







