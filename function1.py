numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

results = map(lambda x, y : x + y, numbers1, numbers2)

print("Additon of two lists")

print(list(results))

nums = [1, 2 ,3, 4, 5]

def sq(n):
    return n*n

square = list(map(sq, nums))
print("square root of numbers in a list")
print(square)