def swap(): #taking input, calling actual swap2 function
    x = int(input('Input a number: '))
    y = int(input('Input a number: '))
    x,y = swap2(x, y)
    print(x,y)
  
def swap2(x,y):
    if (x > y or y < x):
        temp = x #using temp variable to store one value
        x = y
        y = temp
        return x,y
    else:
      return x,y
      
swap()