# gestor-recetas-python/models/ingrediente.py

from dataclasses import dataclass

@dataclass
class Ingrediente:
    nombre: str
    cantidad: float
    unidad: str
    
    def __repr__(self) -> str:
        return (f'{self.cantidad} {self.unidad} de {self.nombre}')
    
    def modificar_stock(self, cantidad: float) -> float:
        nuevo_stock = self.cantidad + cantidad
        if nuevo_stock < 0:
            raise ValueError('Error: el stock no puede ser menor que 0.')
        self.cantidad = nuevo_stock
        return self.cantidad
    
    