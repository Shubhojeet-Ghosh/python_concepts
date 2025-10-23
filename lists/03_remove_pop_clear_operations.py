L = [1,2,3,4,5]
print(f"Original List : {L}")

# pop removes and returns by index; default last element (amortized O(1) for pop())
x = L.pop()          # x = 5, L -> [1,2,3,4]
print(f"Popped last element : {x}, New List : {L}")

y = L.pop(0)         # removes front O(n), L -> [2,3,4]
print(f"Removing : {y}, New List : {L}")

# # remove removes first matching value (O(n))
L.remove(3)          # L -> [2,4]
print(f"List after removing the first instance of 3 : {L}")

# # clear empties list (O(n) to release refs)
L.clear()            # L -> []
print(f"Cleared List : {L}")

# # delete by index or slice using del
L = [1,2,3,4]
del L[1]             # L -> [1,3,4]
print(f"Deleting from index 1 , L : {L}")

L.remove(4)
print(f"Deleting 4 from the List, L : {L}")