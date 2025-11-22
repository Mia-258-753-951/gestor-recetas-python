#gestor-recetas-python/main.py

from models.ingrediente import Ingrediente
from models.receta import Receta

def main():
    ingrediente1 = Ingrediente(nombre='harina', cantidad=125.00, unidad='gramos')
    ingrediente2 = Ingrediente(nombre='aceite', cantidad=0.250, unidad='litros')
    
    receta = Receta(nombre='Migas', ingredientes=[ingrediente1], pasos=[])
    print(receta)
    receta.añadir_ingrediente(ingrediente2)
    receta.añadir_paso('añadir el aceite')
    print(receta)
    
if __name__ == '__main__':
    main()