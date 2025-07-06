def identificar_as_bgp(numero_as):
    """
    Función para identificar si un AS BGP es público o privado.

    Parámetros:
        numero_as: El número de AS BGP a verificar.

    Retorno:
        "Público" si el AS es público, "Privado" si es privado,
        o "No encontrado" si no se encuentra en la lista de rangos.
    """

    # Lista de rangos de AS públicos
    rangos_as_publicos = [
        (64512, 65535),
        (131072, 131079),
        (2097152, 2097159),
        (2121952, 2121959),
        (3232236, 3232243),
        (3355440, 3355447),
        (4294967296, 4294967299)
    ]

    # Lista de rangos de AS privados
    rangos_as_privados = [
        (1024, 64511),
        (65536, 131071),
        (131080, 2097151),
        (2097160, 2121951),
        (2121960, 3232235),
        (3232244, 3355439),
        (3355448, 4294967295)
    ]

    # Verificar si el AS está en un rango de AS públicos
    for rango in rangos_as_publicos:
        if rango[0] <= numero_as <= rango[1]:
            return "Público"

    # Verificar si el AS está en un rango de AS privados
    for rango in rangos_as_privados:
        if rango[0] <= numero_as <= rango[1]:
            return "Privado"

    # Si no se encuentra en ningún rango, indicar que no se ha encontrado
    return "No encontrado"


# Solicitar al usuario el número de AS
numero_as = int(input("Ingrese el número de AS BGP: "))

# Identificar el tipo de AS y mostrar el resultado
tipo_as = identificar_as_bgp(numero_as)
print(f"El AS{numero_as} es: {tipo_as}")
