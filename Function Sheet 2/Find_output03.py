# What is the output of this code

def fun1():
    name = "Suyash"
    def fun2():
        name = "Chaudhary"
    fun2()
    print(name)

fun1()

#Output : Suyash
