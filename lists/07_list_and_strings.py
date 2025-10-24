a = "this"

# b = ['t', 'h', 'i', 's']
b = list(a) 
print(f"String converted to a list of characters : {b}")

my_str = "This is a sentence."
# c = ['This', 'is', 'a', 'sentence.']
c = my_str.split()
print(f"C : {c}")

joined = " ".join(c)
print(f"Joined String : {joined}")