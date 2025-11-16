#  6.What is Error in this code and how can we correct this code?

#  def test():
#  lang = "Python"
#  print(lang)
#  test()
#  print(lang)

# Error : NameError: name 'lang' is not defined

# Correct code: 

def test():
    global lang
    lang = "Python"
    print(lang)

test()
print(lang)
