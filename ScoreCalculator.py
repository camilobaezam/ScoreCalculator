import os

def calcular_puntaje(palabra):
    longitud = len(palabra)
    if longitud < 3:
        return 0
    elif 3 <= longitud <= 6:
        return longitud * 1
    elif 7 <= longitud <= 9:
        return longitud * 2
    else:
        return longitud * 3


def procesar_archivo(ruta):
    if not os.path.exists(ruta):
        print(f"Error: El archivo '{ruta}' no existe.")
        return [], 0, None
    
    palabras = []
    puntaje_total = 0
    max_puntaje = -1
    palabra_max = ""
    
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for linea in f:
                palabra = linea.strip()
                if palabra:
                    palabras.append(palabra)
                    puntaje = calcular_puntaje(palabra)
                    puntaje_total += puntaje
                    
                    if puntaje > max_puntaje:
                        max_puntaje = puntaje
                        palabra_max = palabra
                    elif puntaje == max_puntaje and palabra < palabra_max:
                        palabra_max = palabra  # En empate, la menor alfabéticamente
        
        return palabras, puntaje_total, (palabra_max, max_puntaje) if max_puntaje >= 0 else None
    
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return [], 0, None


def mostrar_resultados(palabras, puntaje_total, max_info):
    if not palabras:
        print("No se encontraron palabras válidas en el archivo.")
        return
    
    print("\nResultados:")
    print("-" * 60)
    print(f"{'Palabra':<40} {'Longitud':<10} {'Puntaje':<8}")
    print("-" * 60)
    
    for palabra in palabras:
        longitud = len(palabra)
        puntaje = calcular_puntaje(palabra)
        print(f"{palabra:<40} {longitud:<10} {puntaje:<8}")
    
    print("-" * 60)
    print(f"Total de palabras procesadas: {len(palabras)}")
    print(f"Puntaje total acumulado: {puntaje_total} puntos")
    
    if max_info:
        palabra_max, puntaje_max = max_info
        print(f"Palabra con mayor puntaje: {palabra_max} → {puntaje_max} puntos")


def main():
    print("=== ScoreCalculator - Calculador de Puntajes de Palabras ===\n")
    
    while True:
        ruta = input("Ruta del archivo de palabras (o 'salir'): ").strip()
        
        if ruta.lower() in ['salir', 'exit', 'q']:
            print("¡Hasta luego!")
            break
        
        if not ruta:
            print("Debes ingresar una ruta.\n")
            continue
        
        palabras, puntaje_total, max_info = procesar_archivo(ruta)
        
        if palabras:
            mostrar_resultados(palabras, puntaje_total, max_info)
            print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
