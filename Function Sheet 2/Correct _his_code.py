# What is Error in this code and how can we correct this code

# Wrong code:

# def pythagoras(a,b):
#  return square(a) + square(b)
#  c2 = pythagoras(3,4)
#  def square(x):
#  return x * x
#  print("c2 = ", c2)


#Right code:

def square(x):
    return x * x

def pythagoras(a, b):
    return square(a) + square(b)

c2 = pythagoras(3, 4)
print("c2 =", c2)
