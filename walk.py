import os
from tqdm import tqdm 

def walkdir(folder):
    for dirpath, _, files in os.walk(folder):
        for filename in files:
            yield (dirpath, filename)

def main(folder):
    list_train=[]
    for dirpath, filename in tqdm(walkdir(folder)):
        list_train.append(filename)
        print(filename)
        
        "cuadrar archivos de imagenes CON labels del csv"
        "obtener por imagen todos sus BBox"
            
            "chequear que el tamaño de los archivos son los que dicen en el csv para pner los BBox"
            "chequear que los BBox estan dentro de la imagen"
            "chequear que los BBox no se solapan"
            "chequear que los BBox no estan vacios"

        "separar las imagener ne test, train y validacion"
        "verificar si las imagenes estan corruptas"
        "separar clases y verificar si estan balanceadas o no (label: HAY O NO HAY PRODUCTOS)"
        "marcar el BB en los productos faltantes" 

    return len(list_train)

if __name__ == '__main__':
    folder = '/home/ferpe/Escritorio/AnyoneAI/FP2/Object_detection_for_in-store_inventory_management-/images'
    print(main(folder))