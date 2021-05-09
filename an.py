an = int(input("Introdu un an"))
text = f"anul {an} este bisect"

if an % 4 == 0:
    print(text)
else:
    text = f"anul {an} este normal"
    print(text)