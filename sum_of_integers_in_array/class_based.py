'''
  Purpose : Class Based approach to add up all integers in a list which contains integers, strings and lists
  Author : Rohit Pai
  Date : 9th July 2024
'''

class ListProcessor :
  '''
    This class is used to contain all the possible processes we can do on the list
  '''
  
  def __init__(self):
    '''
      We define the variables that we want to access within the methods of this class
    '''
    self.sum = 0
    
  
  def sumArray(self, arr):
    '''
      This method receives a list as input
      The list can have integers, strings as well as other such lists as elements
      We traverse through each element in the list. 
        If the element is an integer, we add it to the sum
        If the element is a list, I go to similarly traverse through each element
    '''

    for element in arr :
      if isinstance(element, int) :
        self.sum += element
      elif isinstance(element, list) :
        self.sumArray(element)
  
def main():
  '''
    Here we define the operations to be performed when we run the file,
    We call the sumArray function with the given input amd print the sum
  '''
  lp = ListProcessor()
  lp.sumArray([1,2,3,[[20],5],'foo',4])
  print(lp.sum)
  

if __name__ == "__main__":
  '''
    This says that if this file is run directly, then the block below must be executed 
  '''
  main()