x = 67
y = "six seven"
z = 6.7
a = True
b = "67"

print("\n", type(x),"\n", type(y), "\n", type(z), "\n", type(a))
print("\n", type(67),"\n", type("six seven"), "\n", type(6.7), "\n", type(True))
print(int(b), int (z))
print(str(x), str(z), str(a))
print(float(x), float(b))
print(bool(x), bool(y), bool(z), bool(a), bool(b))

print("\n", type(x),"\n", type(y), "\n", type(z), "\n", type(a))
print("\n", type(67),"\n", type("six seven"), "\n", type(6.7), "\n", type(True))
print(int("67"), int (6.7))
print(str(67), str(6.7), str(True))
print(float(67), float("67"))
print(bool(67), bool("six seven"), bool(6.7), bool(True), bool("67"))

x = float(67)
y = bool("six seven")
z = int(6.7)
a = str(True)
b = bool("67")

print("\n", type(x),"\n", type(y), "\n", type(z), "\n", type(a), "\n", type(b))