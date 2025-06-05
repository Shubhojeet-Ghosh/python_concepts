# regular way 
squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x * x)
# squares is now [1, 4, 9, 16, 25]
print(squares)

squares = [x*x for x in [1, 2, 3, 4, 5]]
print(squares)

even_squares = [x*x for x in range(1,11) if x % 2 == 0]
print(even_squares)
