import csv

def leer_archivo(paises_america):
    """
    Lee un CSV y devuelve una lista de diccionarios con los datos de los países.
    """
    paises = []  # Lista vacía donde guardaremos cada país
    try:
        with open(paises_america, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                pais = {
                    "Nombre": row["Nombre"],
                    "Poblacion": int(row["Poblacion"]),
                    "Superficie_km2": int(row["Superficie_km2"]),
                    "Continente": row["Continente"]
                }
                paises.append(pais)
    except FileNotFoundError:
        print("⚠️ Archivo no encontrado:", paises_america)
    return paises

lista_paises = leer_archivo("paises_america.csv")
print(f"Cantidad de paises: {len(lista_paises)}")