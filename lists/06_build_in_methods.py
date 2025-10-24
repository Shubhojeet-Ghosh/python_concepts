L = [3,1,4,1,5]

# len, min, max, sum (built-ins)
n = len(L)           # 5
mn = min(L)          # 1
mx = max(L)          # 5
total = sum(L)       # 14

# sort (in-place) - Timsort O(n log n) stable
L.sort()             # L -> [1,1,3,4,5]
print(f"Sorted Array L : {L}")

# sorted returns new list
L2 = sorted(L, reverse=True)
print(f"Sorted new array then reversed : {L2}")

# reverse (in-place) O(n)
L.reverse()          # reverse order
print(f"Reversed List : {L}")

# count occurrences (O(n))
c = L.count(1)       # 2
print(f"Count of 1 in L : {c}")

# index to find first occurrence (O(n))
i = L.index(3)       # index of value 3
print(f"The index of the first occurrence of 3 : {i}")

# copy (shallow)
copy = L.copy()      # new list; inner objects referenced
print(f"Shallow Copy of the List : {copy}")