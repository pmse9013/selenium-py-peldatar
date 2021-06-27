data = open("adat.txt", "r")
x = data.read()
list = []
for i in x:
    a = x.split(" ")
    for i in a:
        i.rstrip()
    list.append(a)
print(list)







