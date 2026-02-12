aves = ["Loro gris", "Paloma de diamantes", "Loro Verde"]
print("Los valores de la lista antes de insertar son:")
for ave in aves:
    print(ave, end = "")

aves.append("Guacamayo")
aves.append("Periquitos Australianos")
aves.append("Cacatua")
print("Los valores de la lista despues de insertar son:")
for ave in aves:
    print(ave, end=" ")
print("\n")
def pop_arreglo_aves(arreglo_original):
    if arreglo_original:
        arreglo_original.pop()      
        print("Se elimino el ultimo elemento\n")
    return arreglo_original

def push_arreglo_aves(arreglo_original):
    arreglo_final = arreglo_original.copy()
    arreglo_final.append("Guacamayo")
    arreglo_final.append("Periquitos Australianos")
    arreglo_final.append("Cacatua")
    print("Los valores del arreglo despues de insertar son: \n")
    for i in arreglo_final:
        print(i, end=" ")
    print("\n")
    return arreglo_final

def arreglo_aves(arreglo_original):
    print("Los valores iniciales del arreglo son: \n")
    for ave in arreglo_original:
        print(ave, end=" ")

def main():
    aves = ["Loro gris", "Paloma de diamantes", "Loro Verde"]
    nuevo_aves = []
    arreglo_aves(aves)
    print("\n")
    nuevo_aves = push_arreglo_aves(aves)


if __name__ == "__main__":
    main()  