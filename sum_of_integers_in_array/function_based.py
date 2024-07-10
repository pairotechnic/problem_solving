'''
  Solved using global variables and functions approach
'''

sum = 0

def sumArray(arr):

  # We declare sum as global, because if we access a variable sum in a function,
  # the tendency of python is to find a local variable sum in that function
  global sum 
  
  for i in arr :
    if type(i) == int :
      sum += i
    elif type(i) == list :
      sumArray(i)

def main():

  sumArray([1,2,3,[[20],5],'foo',4])

  print(sum)
  
if __name__ == "__main__":
  main()