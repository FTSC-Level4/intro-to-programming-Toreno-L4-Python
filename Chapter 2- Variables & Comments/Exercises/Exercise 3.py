namefirst = input("Input your first name:")
namelast = input("Input your last name:")

print("\t",namefirst, "\t\n\t", namelast, "\t")
namefirst2 = namefirst.lstrip("\t\n")
namelast2 = namelast.rstrip("\t\n")
print("\t",namefirst, "\t\n\t", namelast, "\t")

