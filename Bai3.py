from ._anvil_designer import Form1Template
from anvil import *
import random


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def insertionSort(self, arr):
    n = len(arr)
    if n <=1:
      return
    for i in range(1,n):
      key = arr[i]
      j = i-1
      while j>=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
      arr[j+1] = key

  def btnSort_click(self, **event_args):
    """This method is called when the button is clicked"""
    input = self.txtInput.text
    isAllNumber = input.replace(" ","")
    if(isAllNumber.isnumeric()):
      input = " ".join(input.split())
      arr = input.split(' ')
      arr = [int(numeric_string) for numeric_string in arr]
      self.insertionSort(arr)
      listtoStr = ' '.join([str(elem) for elem in arr])
      self.txtOutput.text = listtoStr
    else:
      self.txtOutput.text = "Phải là một mảng số"

  def btnRandom_click(self, **event_args):
    """This method is called when the button is clicked"""
    rand_list = []
    n=10
    for i in range(n):
      rand_list.append(random.randint(3,9))
    rand_list = ' '.join([str(elem) for elem in rand_list])
    self.txtInput.text = rand_list
      
