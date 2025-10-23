l = [10,20,30,40,50]

for num in l:
    print(num)

for index,num in enumerate(l):
    print(f"Index : {index}, number : {num}")

gen = (x*x for x in range(10))
print(gen)