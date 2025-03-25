print("Napiste 2 cisla")
cislo1 = int(input("Napiste prvni cislo"))
cislo2 = int(input("Napiste druhe cislo"))
print("Napiste kterou operace chcete delat")
operace = input("+ or - or / or * ")
if operace == "+":
    print(f"Odpoved: {cislo1 + cislo2}")
elif operace == "-":
    print(f"Odpoved: {cislo1 - cislo2}")
elif operace == "/":
    print(f"Odpoved: {cislo1 / cislo2}")
else:
    print(f"Odpoved: {cislo1 * cislo2}")