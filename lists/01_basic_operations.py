# 1. Empty list
L = []
L2 = list()

# 2. From iterable (list, tuple, range, generator)
L3 = list([1, 2, 3])
L4 = list((4, 5))
L5 = list(range(5))    # [0,1,2,3,4]

print(f"L5 : {L5}")

# 3. Pre-sized list with same value
zeros = [0] * 5        # [0,0,0,0,0]
print(f"Zeros : {zeros}")

# 4. Nested lists (matrix)
matrix = [[1,2,3], [4,5,6]]
print(f"Matrix : {matrix}")