from doctores import acciones

print("""
Seleccione una acción:
    - Registro (registro)
    - Login (login)
    - Salir (salir)
""")
realizar = acciones.Acciones()

accion = input("¿Qué desea realizar?: ")
if accion == "registro":
    realizar.registro()
elif accion == "login":
    realizar.login()
elif accion == "salir":
    print("Vuelva pronto.")