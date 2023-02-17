import random
list_with_numbers = list(range(10))

print("Refactoring the program")
new_list = map(lambda a: a + random.random(), filter(lambda i: not i % 2, list(range(10))))

print(list(new_list))