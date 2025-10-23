L = [10,20,30,40,50]

# indexing (O(1))
a = L[0]             # 10
b = L[-1]            # 50 (last element)
print(f"Last Element : {b}")

# slicing -> returns new list (copy)
s1 = L[0:5:2]          # [20,30,40]
print(f"All elements in steps of 2 L: {s1}")

s2 = L[:3]           # [10,20,30]
print(s2)

s3 = L[::2]          # [10,30,50]
print(s3)

print(f"Reverse of the list : {L[::-1]}")

# note: slicing copies — modifying slice won't change original
s1[0] = 99           # L unaffected
