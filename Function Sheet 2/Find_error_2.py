# 7.What is Error in this code and how can we correct this code?

#  name ="Suyash"
#  print(name)
#  def fun():
#  print(name)
#  name ="Chaudhary"
#  lang = "Python"
#  print(lang)
#  fun()
#  print(name)

# UnboundLocalError: cannot access local variable 'name' where it is not associated with a value

#  Correct code:

name = "Suyash"
print(name)

def fun():
    global name
    print(name)
    name = "Chaudhary"
    lang = "Python"
    print(lang)

fun()
print(name)
