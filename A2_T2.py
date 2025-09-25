print("Program starting.")

brand = input("Insert car brand: ")
model = input("Insert car model: ")

# Ensimmäinen print tulostaa alkuosan, end estää rivinvaihdon
print('Car brand is "' + brand + '"', end=" ")
# Toinen print tulostaa jatkon, sep lisää välilyönnin automaattisesti
print("and", "the model is '" + model + "'.", sep=" ")

print("Program ending")
