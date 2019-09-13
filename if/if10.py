a = int(input("a?"))
b = int(input("b?"))
c = int(input("c?"))

if ((a * a) + (b * b) == (c * c)):
    print("C az átofogó")

elif ((c * c) + (b *b) == (a * a)):
    print("A az átfogó")

elif ((c * c) + (a *a) == (b * b)):
    print("B az átfogó")

else:
    print("Invalid")
