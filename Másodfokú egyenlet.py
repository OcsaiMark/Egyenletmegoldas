def f1(label):
    print(label)
    print("Van e megoldása a mésodfokú egyenletnek?")
    a = int(input("Kérem az a együtthatót: "))
    b = int(input("Kérem a b együtthatót: "))
    c = int(input("Kérem a c együtthatót: "))
    diszkriminans = b*b - 4*a*c
    if diszkriminans == 0:
        print("Az egyenletnek megoldása van.")
    else:
        if diszkriminans < 0:
            print("Az egyenletnek nincs megoldása.")
        else:
            print("Az egyenletnek két megoldása van.")

f1("1. feladat")

