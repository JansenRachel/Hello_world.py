print("Hello World")

name = "Rachel"
print("Hello", name)
print("Hello " + name)

num = 7
print("Hello", num)
print("Hello " + str(num))

fave_food1 = "steak"
fave_food2 = "pie"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}.")



x = "Hello World"
multiples = "three"
print(x.upper())
print("Hello World".lower())
print(f"{multiples} times {multiples} equals nine".count(multiples))
print(x.split("o"))

my_dict = { "name": "Noelle", "language": "Python" }
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)


