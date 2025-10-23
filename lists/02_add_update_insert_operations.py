L = [1,2,3,4]
print(f"L : {L}")

L.append(5)
print(f"Appedned 5 to the list : {L}")

L.extend([5,6,['a','b']])      # L -> [1,2,3,4,5,6]
print(f"Extended List : {L}")

L.insert(0,0)
print(f"Inserted 0 at index 0 : {L}")

# Update Operations
L = [10, 20, 30]

# index assignment (O(1))
L[1] = 99            # L -> [10,99,30]
print(f"Update / Assignment of data : {L}")

# slice assignment (can change length)
L[0:2] = [1,2,3]     # L -> [1,2,3,30]
print(f"Slice Assignment : {L}")

# in-place multiplication (resizes)
L *= 2               # duplicates content: [1,2,3,30,1,2,3,30]
print(f"In place multiplication : {L}")