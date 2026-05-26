import os
from PIL import Image
import imagehash

def buscar_thumbnails_y_originales(ruta_carpeta, tolerancia=4):
    """
    Escanea la carpeta buscando imágenes visualmente idénticas (originales y thumbnails).
    La tolerancia determina qué tan estrictos somos (menor número = más idénticos).
    """
    extensiones_validas = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
    historial_hashes = {}
    grupos_duplicados = []

    print("Iniciando scan")
    print("Calculando hashes...\n")

    # Recorremos la carpeta y subcarpetas en ella
    for raiz, _, archivos in os.walk(ruta_carpeta):
        for archivo in archivos:
            if archivo.lower().endswith(extensiones_validas):
                ruta_completa = os.path.join(raiz, archivo)
                
                try:
                    # Abrimos la imagen y calculamos pHash
                    with Image.open(ruta_completa) as img:
                        hash_actual = imagehash.phash(img)
                    
                    # Comparamos el hash actual con los que tenemos guardados
                    encontrado = False
                    for hash_guardado, rutas in historial_hashes.items():
                        # Restar los hashes nos da la 'distancia de Hamming' (diferencia visual entre las fotos)
                        # La tolerancia está puesta cuando definimos la variable
                        if hash_actual - hash_guardado <= tolerancia:
                            rutas.append(ruta_completa)
                            encontrado = True
                            break
                    
                    if not encontrado:
                        # Si no lo encuentra se crea una nueva entrada en el diccionario, que en posteriores vueltas del loop será comparado
                        historial_hashes[hash_actual] = [ruta_completa]
                        
                except Exception:
                    # Si un archivo está corrupto o Android lo dejó a medias, lo saltamos
                    continue

    # Filtramos para quedarnos solo con los archivos que tienen dupes
    for hash_w, rutas in historial_hashes.items():
        if len(rutas) > 1:
            grupos_duplicados.append(rutas)

    return grupos_duplicados

 #Esta línea sirve para que si tu otro día quieres hacer un import duplicados, al hacer el import lo único que ocurre es que obtienes la función de arriba
 #PERO no se ejecuta, solo te llevas la función
if __name__ == "__main__":
    RUTA_FOTOS = input("Introduce la ruta de la carpeta a escanear: ")
    
    duplicados = buscar_thumbnails_y_originales(RUTA_FOTOS)

    if not duplicados:
        print("No se han encontrado imágenes repetidas, puedes probar a cambiar la tolerancia, o igual no tienes repetidas")
    else:
        print(f"Se han encontrado {len(duplicados)} grupos de imágenes repetidas:\n")
        # Las mostramos
        for i, grupo in enumerate(duplicados, 1):
            print(f"--- GRUPO {i} ---")

            for ruta in grupo:
                tamano = os.path.getsize(ruta) // 1024
                print(f" -> [{tamano} KB] {ruta}")
            print()