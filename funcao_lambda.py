x = lambda a : a + 10
print(x(5))


squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))

print(squares)
