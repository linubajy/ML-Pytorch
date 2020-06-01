
"""
Implement the linear regression model using python and numpy in the following class.
The method fit() should take inputs like,
x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
from sklearn.linear_model import LinearRegression
import numpy

class LinearRegression(object):
  """
  An implementation of linear regression model
  """
  _input=[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
  _output=[1,2,3,4,5,6,7,8,9,10]
  model=LinearRegression()
  model.fit(_input,_output)
  output=model.predict([[15]])
  print(output)

  def fit(_input, _output):
    pass

  def predict(_input):
    pass
	
    

 
