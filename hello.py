my_int = 10
my_float = 3.14
my_str = "Hello"
my_bool = True

print(my_int, my_float, my_str, my_bool)
print(type(my_int), type(my_float), type(my_str), type(my_bool))

if my_int > 5:
    print("my_int is greater than 5")
else:
    print("my_int is 5 or less")

for i in range(3):
    print("Loop iteration:", i)

count = 0
while count < 3:
    print("Count is:", count)
    count += 1

def greet(person):
    return f"Hello, {person}!"

print(greet("Alice"))