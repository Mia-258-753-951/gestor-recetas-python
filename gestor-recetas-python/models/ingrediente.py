# gestor-recetas-python/models/ingrediente.py

from dataclasses import dataclass

@dataclass
class Ingrediente:
    nombre: str
    cantidad: float
    unidad: str
    
    def __repr__(self) -> str:
        return (f'Ingrediente: {self.nombre}- Stock: {self.cantidad}- unidad: {self.unidad}')
    
    def modificar_stock(self, cantidad: float) -> float:
        if self.cantidad < 0:
            raise ValueError('Error: el stock no puede ser menor que 0.')
        self.cantidad += float
        return self.cantidad
    
    