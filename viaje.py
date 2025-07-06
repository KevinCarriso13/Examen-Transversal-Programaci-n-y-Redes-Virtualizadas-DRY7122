import math

def obtener_coordenadas(ciudad):
    ciudades = {
        "santiago": (-33.4489, -70.6693),      # Chile
        "arica": (-18.4783, -70.3126),
        "iquique": (-20.2140, -70.1521),
        "valparaíso": (-33.0472, -71.6127),
        "lima": (-12.0464, -77.0428),          # Perú
        "cusco": (-13.5319, -71.9675),
        "arequipa": (-16.4090, -71.5375),
        "piura": (-5.1945, -80.6328)
    }
    return ciudades.get(ciudad.lower())

def calcular_distancia(coord1, coord2):
    R = 6371.0  # Radio de la Tierra en km
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia_km = R * c
    return distancia_km

def estimar_duracion(distancia_km, medio):
    velocidades = {
        "auto": 80,
        "bus": 60,
        "bicicleta": 20,
        "a pie": 5
    }
    velocidad = velocidades.get(medio, 60)
    horas = distancia_km / velocidad
    return round(horas, 2)

def convertir_a_millas(km):
    return round(km * 0.621371, 2)

print("=== CALCULADORA DE VIAJES CHILE - PERÚ ===")

while True:
    origen = input("\nIngrese la Ciudad de Origen (o 's' para salir): ").strip().lower()
    if origen == 's':
        print("Saliendo del programa.")
        break

    destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ").strip().lower()
    if destino == 's':
        print("Saliendo del programa.")
        break

    coord_origen = obtener_coordenadas(origen)
    coord_destino = obtener_coordenadas(destino)

    if not coord_origen or not coord_destino:
        print("Una o ambas ciudades no están registradas.")
        continue

    print("Medios disponibles: auto, bus, bicicleta, a pie")
    medio = input("Seleccione el medio de transporte: ").strip().lower()
    if medio not in ["auto", "bus", "bicicleta", "a pie"]:
        print("Medio no válido. Se usará 'bus' por defecto.")
        medio = "bus"

    distancia_km = calcular_distancia(coord_origen, coord_destino)
    distancia_millas = convertir_a_millas(distancia_km)
    duracion_horas = estimar_duracion(distancia_km, medio)

    print(f"\n🗺️ Narrativa del viaje:")
    print(f"Desde {origen.title()} hasta {destino.title()} en {medio}.")
    print(f"Distancia: {round(distancia_km, 2)} km ({distancia_millas} millas).")
    print(f"Duración estimada: {duracion_horas} horas aproximadamente.")

    continuar = input("\n¿Desea calcular otro viaje? (s para salir): ").lower()
    if continuar == 's':
        print("Hasta pronto.")
        break
