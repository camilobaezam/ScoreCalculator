# ScoreCalculator

Un calculador de puntajes de palabras en Python.  
Lee palabras desde un archivo de texto (una palabra por línea), calcula el puntaje de cada una según su longitud y muestra:

- Puntaje total acumulado
- Palabra con mayor puntaje
- Tabla con todas las palabras procesadas

### Regla de puntuación

- Longitud < 3 caracteres → 0 puntos
- Longitud 3–6 caracteres → 1 punto por letra
- Longitud 7–9 caracteres → 2 puntos por letra
- Longitud 10 o más caracteres → 3 puntos por letra

## Requisitos

- Python 3.6 o superior  
- No requiere librerías externas

## Instalación

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/camilobaezam/ScoreCalculator.git
   cd ScoreCalculator
2. Crea un archivo palabras.txt con una palabra por línea.
Ejemplo:
HI
DOG
PYTHON
DRUDGERY
ENCYCLOPEDIA
SUPERCALIFRAGILISTICEXPIALIDOCIOUS

## Uso

Ejecuta el programa: python ScoreCalculator.py
Te pedirá la ruta del archivo de palabras.
Puedes pasar la ruta directamente:python ScoreCalculator.py palabras.txt

Ejemplo de ejecución
Archivo palabras.txt:
HI
DOG
PYTHON
DRUDGERY
ENCYCLOPEDIA
SUPERCALIFRAGILISTICEXPIALIDOCIOUS

Salida:
=== ScoreCalculator - Calculador de Puntajes de Palabras ===

Ruta del archivo de palabras: palabras.txt

Procesando palabras...

Resultados:
----------------------------------------
Palabra                                     Longitud   Puntaje
----------------------------------------
HI                                          2          0
DOG                                         3          3
PYTHON                                      6          6
DRUDGERY                                    8          16
ENCYCLOPEDIA                                12         36
SUPERCALIFRAGILISTICEXPIALIDOCIOUS          34         102
----------------------------------------

Total de palabras procesadas: 6
Puntaje total acumulado: 163 puntos
Palabra con mayor puntaje: SUPERCALIFRAGILISTICEXPIALIDOCIOUS → 102 puntos

Archivo vacío o solo líneas en blanco
→ Mensaje: "No se encontraron palabras válidas."

Notas

- Ignora líneas vacías y solo espacios
- Conserva el formato original al mostrar palabras
- Usa UTF-8 (soporta acentos, ñ, etc.)
- Si el archivo no existe → mensaje claro y termina

Ideas para extender

- Mostrar las 10 palabras con mayor puntaje
- Calcular solo palabras únicas
- Exportar resultados a CSV
- Interfaz gráfica (tkinter)
- Opción para múltiples archivos
- Multiplicadores (palabras con "z" ×2, etc.)

Autor
Camilo Baeza
