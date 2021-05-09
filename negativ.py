nr = float(input("Introdu un numar: "))

if nr > 0:
    if nr < 10:
        print("Mai mic ca 10")
    else:
        print("Mai mare sau egal cu 10")
elif nr == 0:
    print("Numarul este 0")
else:
    nr = abs(nr)
    print(f"Numarul transformat in pozitiv este {nr}")