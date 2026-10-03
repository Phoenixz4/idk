print("[1] complement")
print("[2] suplement")
print(" ")
inpt = input("->")
if inpt == "1":
    x = int(input("numar : "))
    u = 90-x
    print("complementul lui", x, "este", u)
elif inpt == "2":
    x = int(input("numar : "))
    u = 180-x
    print("suplementul lui", x, "este", u)