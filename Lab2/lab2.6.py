#Дан некоторый список

list = [(1,1,1), (1,2,3), (-1,-1,7), (-3,-2,8), (0,0,0), (3,-4,-5)]

print("A list is given-", list)
# Список по сумме кортежей
print("Sorted list by sum of tuples-",sorted(list, key=sum))

# Список по третьим элементам из котрежей
print("Sorted list by the third elements of tuples-",sorted(list, key=lambda tup: tup[2]))

#Дан словарь

a={'b': 3, 'c': 2, 'a': 4, 'd': 1}


print("В алфавитном порядке-",sorted(a))
print("В порядке убывания-", sorted(a.items(), key= lambda item: item[1], reverse=True))

