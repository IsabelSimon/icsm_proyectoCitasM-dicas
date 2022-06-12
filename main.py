print("Simón Morales Isabel Cristina  9°A DGS Desarrollo para dispositivos inteligentes 14-06-2022 \n")

from doctors import acciones

print("""
Acciones disponibles:
    - Registro de médico - (registro)
    - Login - (login)
""")

hazEl = acciones.Acciones()

accion = input("¿Qué desea hacer?: ")

if accion == "registro":
    hazEl.registro()
    
elif accion == "login":
    hazEl.login()
else:
    print("Opción no disponible, intente nuevamente")

