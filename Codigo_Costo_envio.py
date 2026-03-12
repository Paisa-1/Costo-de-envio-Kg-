peso = float(input("Ingrese el peso del paquete en kg: "))
urgente = input("¿El envío es urgente? (si/no): ")

def calcular_costo(peso):
    if peso <= 2:
        return 5000
    elif peso <= 5:
        return 8000
    elif peso <= 10:
        return 12000
    else:
        return 15000


def calcular_recargo(costo, urgente):
    if urgente == "si":
        return costo * 0.20
    else:
        return 0



def transporte_especial(peso):
    if peso > 20:
        print("El paquete requiere transporte especial.")


costo = calcular_costo(peso)
recargo = calcular_recargo(costo, urgente)

costo_final = costo + recargo

transporte_especial(peso)

print("Costo base:", costo)
print("Recargo:", recargo)
print("Costo final:", costo_final)