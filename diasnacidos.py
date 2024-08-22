from datetime import date
import os
os.system("cls")
def calcular (FechaNacimiento):
    FechaActual = date.today()
    DiasVivido = (FechaActual - FechaNacimiento).days
    return DiasVivido

nacido= input ("Ingrese Su Fecha De Nacimiento en YYYY-MM-DD  :")
FechaNacimiento = nacido
FechaNacimiento= date.fromisoformat(FechaNacimiento)
DiasVivido= calcular(FechaNacimiento)
os.system("cls")

print(f"Tu Fecha De Nacimiento es :", nacido)

print(f"___Has Estado Vivo Durante {DiasVivido} Dias__")

