# Función principal para gestionar las reservas
def obtenerdetalles():
    respuesta=input("agregar nuevo cliente (1) o cliente standard (2): ")
    if (respuesta=="1"):
        cliente1=input("nombre de cliente: ")
        habitacion1=input("que habitacion gusta?: ")
        fecha1=input("en que fecha: ")
        detalles1 = {"cliente": cliente1,
        "habitacion": habitacion1,
        "fecha": fecha1}
    elif (respuesta=="2"):
        detalles1 = {
        "cliente": "Juanito",
        "habitacion": "4",
        "fecha": "23 de Diciembre 2024"
        }
    return detalles1
    


def gestionar_reservas(operacion, detalles, reservas=None):
    if reservas is None:
        reservas = []  # Inicializar la lista de reservas si está vacía

    # Operación: Reservar una habitación
    if operacion == "reservar":        
        # Verificar si la habitación está disponible en la fecha solicitada
        for reserva in reservas:
            if reserva["habitacion"] == detalles["habitacion"] and reserva["fecha"] == detalles["fecha"]:
                return f"La habitación {detalles['habitacion']} ya está reservada en la fecha {detalles['fecha']}."
        
        # Si está disponible, agregar la nueva reserva
        detalles = obtenerdetalles()
        nueva_reserva = {
            "cliente": detalles["cliente"],
            "habitacion": detalles["habitacion"],
            "fecha": detalles["fecha"]
        }
        reservas.append(nueva_reserva)
        return f"Reserva confirmada para {detalles['cliente']} en la habitación {detalles['habitacion']} el {detalles['fecha']}."
    
    # Operación: Cancelar una reserva
    elif operacion == "cancelar":
        # Buscar la reserva y eliminarla
        for reserva in reservas:
            if reserva["cliente"] == detalles["cliente"] and reserva["habitacion"] == detalles["habitacion"] and reserva["fecha"] == detalles["fecha"]:
                reservas.remove(reserva)
                return f"Reserva cancelada para {detalles['cliente']} en la habitación {detalles['habitacion']} el {detalles['fecha']}."
        return "No se encontró la reserva para cancelar."
    
    # Operación: Consultar disponibilidad de una habitación en una fecha específica
    elif operacion == "consultar":
        detalles = obtenerdetalles()
        for reserva in reservas:
            if reserva["habitacion"] == detalles["habitacion"] and reserva["fecha"] == detalles["fecha"]:
                return f"La habitación {detalles['habitacion']} no está disponible el {detalles['fecha']}."
        return f"La habitación {detalles['habitacion']} está disponible el {detalles['fecha']}."
    
    # Operación: Listar todas las reservas
    elif operacion == "listar":
        if not reservas:
            return "No hay reservas."
        else:
            listado = "Reservas existentes:\n"
            for reserva in reservas:
                listado += f"Cliente: {reserva['cliente']}, Habitación: {reserva['habitacion']}, Fecha: {reserva['fecha']}\n"
            return listado
    
    # Si la operación no es válida
    else:
        return "Operación no válida."

# se incializa y declara reservas
reservas = []

# Detalles de una reserva (pueden cambiar según la operación)
detalles = {
        "cliente": "Juan",
        "habitacion": "2",
        "fecha": "12 de Diciembre 2024"
}

# Operación a realizar
operacion = input("¿Qué operación desea realizar? (reservar, cancelar, consultar, listar): ")

# Llamar a la función
resultado = gestionar_reservas(operacion, detalles, reservas)
print(resultado)
seguir = input("¿Quieres realizar otra operacion (si o no): ")
while (seguir=="si"):
    operacion = input("¿Qué operación desea realizar? (reservar, cancelar, consultar, listar): ")
    resultado = gestionar_reservas(operacion, detalles, reservas)
    print(resultado)
    seguir = input("¿Quieres realizar otra operacion (si o no): ")
while (seguir=="no"):
    break