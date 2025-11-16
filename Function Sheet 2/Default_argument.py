#  WAP to define and utilize a Python function named introduce to print out information about
#  individuals, including their name, age, and profession, with an optional default value for the
#  profession parameter.

def introduce(name, age, profession="Student"):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I am a {profession}.")
introduce("Krishna", 20, "Engineer")
print()
introduce("Kartik", 22)
