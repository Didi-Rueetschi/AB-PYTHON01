# dictionary_view_pract.py
alter = {"Peter":31, "Julia":28, "Werner":35}

#
w = alter.values()
print("Number of Values:", len(w))
for x in w:
    print(x)
if 31 in w:
    print("31 is included")
alter["Peter"] = 41
if 31 not in w:
    print("31 is not included")
print()

# Keys
k = alter.keys()
print("Number of keys:", len(k))
for x in k:
    print(x)
if "Werner" in k:
    print("Werner is included")
del alter["Werner"]
if "Werner" not in k:
    print("Werner is not included")
print()

# Items
i = alter.items()
alter["Franz"] = 35
print("Number of items:", len(i))
for x in i:
    print(x)
if ("Julia", 28) in i:
    print("Julia is included")
